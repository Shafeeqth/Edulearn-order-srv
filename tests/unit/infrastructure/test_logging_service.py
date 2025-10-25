"""
Unit tests for the enhanced LoggingService with structlog.
"""

import pytest
import time
import threading
import uuid
from unittest.mock import Mock, patch, MagicMock
from src.infrastructure.observability.logging_service import (
    LoggingService,
    AsyncLokiHandler,
    PerformanceProcessor,
    CorrelationProcessor,
    log_performance,
    log_exceptions
)


class TestLoggingService:
    """Test cases for LoggingService."""
    
    def setup_method(self):
        """Setup method for each test."""
        # Reset singleton instance
        LoggingService._instance = None
        LoggingService._initialized = False
    
    def test_singleton_pattern(self):
        """Test that LoggingService follows singleton pattern."""
        service1 = LoggingService()
        service2 = LoggingService()
        
        assert service1 is service2
        assert id(service1) == id(service2)
    
    def test_setup_logger(self):
        """Test logger setup."""
        service = LoggingService()
        logger = service.setup_logger()
        
        assert logger is not None
        assert hasattr(logger, 'info')
        assert hasattr(logger, 'error')
        assert hasattr(logger, 'warning')
        assert hasattr(logger, 'debug')
    
    def test_get_logger(self):
        """Test getting a logger with name."""
        service = LoggingService()
        logger = service.get_logger("test_module")
        
        assert logger is not None
        assert hasattr(logger, 'info')
    
    def test_bind_context(self):
        """Test context binding."""
        service = LoggingService()
        bound_logger = service.bind_context(user_id="123", session_id="456")
        
        assert bound_logger is not None
        # The context should be bound to the logger
    
    def test_unbind_context(self):
        """Test context unbinding."""
        service = LoggingService()
        service.bind_context(user_id="123", session_id="456")
        unbound_logger = service.unbind_context("user_id")
        
        assert unbound_logger is not None
    
    def test_correlation_id(self):
        """Test correlation ID functionality."""
        service = LoggingService()
        correlation_id = str(uuid.uuid4())
        
        service.set_correlation_id(correlation_id)
        retrieved_id = service.get_correlation_id()
        
        assert retrieved_id == correlation_id
    
    def test_correlation_id_thread_safety(self):
        """Test correlation ID thread safety."""
        service = LoggingService()
        results = []
        
        def set_and_get_id():
            correlation_id = str(uuid.uuid4())
            service.set_correlation_id(correlation_id)
            time.sleep(0.01)  # Simulate some work
            results.append(service.get_correlation_id())
        
        # Create multiple threads
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=set_and_get_id)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Each thread should have its own correlation ID
        assert len(results) == 5
        assert len(set(results)) == 5  # All IDs should be unique
    
    def test_log_exception(self):
        """Test exception logging."""
        service = LoggingService()
        
        try:
            raise ValueError("Test exception")
        except Exception as e:
            # Should not raise an exception
            service.log_exception(e, context={"test": "context"})
    
    def test_log_request(self):
        """Test request logging."""
        service = LoggingService()
        
        # Should not raise an exception
        service.log_request(
            method="GET",
            url="/test",
            status_code=200,
            duration=0.1,
            user_id="123"
        )
    
    def test_log_database_query(self):
        """Test database query logging."""
        service = LoggingService()
        
        # Should not raise an exception
        service.log_database_query(
            query="SELECT * FROM test",
            duration=0.05,
            table="test_table"
        )


class TestAsyncLokiHandler:
    """Test cases for AsyncLokiHandler."""
    
    def setup_method(self):
        """Setup method for each test."""
        self.handler = AsyncLokiHandler("http://localhost:3100", batch_size=2, flush_interval=0.1)
    
    def teardown_method(self):
        """Teardown method for each test."""
        self.handler.close()
    
    def test_handler_initialization(self):
        """Test handler initialization."""
        assert self.handler.loki_url == "http://localhost:3100"
        assert self.handler.batch_size == 2
        assert self.handler.flush_interval == 0.1
        assert len(self.handler.batch) == 0
    
    @patch('requests.post')
    def test_emit_log_record(self, mock_post):
        """Test emitting a log record."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        # Create a log record
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Test message",
            args=(),
            exc_info=None
        )
        
        self.handler.emit(record)
        
        # Check that the record was added to the batch
        assert len(self.handler.batch) == 1
    
    @patch('requests.post')
    def test_batch_flushing(self, mock_post):
        """Test batch flushing when batch size is reached."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        # Create log records
        for i in range(3):  # Exceeds batch size of 2
            record = logging.LogRecord(
                name="test",
                level=logging.INFO,
                pathname="test.py",
                lineno=1,
                msg=f"Test message {i}",
                args=(),
                exc_info=None
            )
            self.handler.emit(record)
        
        # Wait for async processing
        time.sleep(0.2)
        
        # Check that the batch was flushed
        assert len(self.handler.batch) == 1  # Last record should remain
    
    @patch('requests.post')
    def test_retry_logic(self, mock_post):
        """Test retry logic for failed requests."""
        # First two attempts fail, third succeeds
        mock_post.side_effect = [
            Mock(status_code=500),
            Mock(status_code=500),
            Mock(status_code=200)
        ]
        
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Test message",
            args=(),
            exc_info=None
        )
        
        self.handler.emit(record)
        
        # Wait for async processing
        time.sleep(0.2)
        
        # Should have attempted 3 times
        assert mock_post.call_count == 3


class TestPerformanceProcessor:
    """Test cases for PerformanceProcessor."""
    
    def setup_method(self):
        """Setup method for each test."""
        self.processor = PerformanceProcessor()
    
    def test_performance_start(self):
        """Test performance start tracking."""
        event_dict = {}
        result = self.processor(None, "performance_start", event_dict)
        
        assert result["event"] == "performance_start"
        assert threading.get_ident() in self.processor.start_times
    
    def test_performance_end(self):
        """Test performance end tracking."""
        thread_id = threading.get_ident()
        self.processor.start_times[thread_id] = time.time() - 0.1
        
        event_dict = {}
        result = self.processor(None, "performance_end", event_dict)
        
        assert result["event"] == "performance_end"
        assert "duration_ms" in result
        assert result["duration_ms"] > 0
        assert thread_id not in self.processor.start_times
    
    def test_regular_log_method(self):
        """Test that regular log methods pass through unchanged."""
        event_dict = {"message": "test"}
        result = self.processor(None, "info", event_dict)
        
        assert result == event_dict


class TestCorrelationProcessor:
    """Test cases for CorrelationProcessor."""
    
    def setup_method(self):
        """Setup method for each test."""
        self.processor = CorrelationProcessor()
    
    def test_set_and_get_correlation_id(self):
        """Test setting and getting correlation ID."""
        correlation_id = "test-correlation-id"
        self.processor.set_correlation_id(correlation_id)
        
        retrieved_id = self.processor.get_correlation_id()
        assert retrieved_id == correlation_id
    
    def test_correlation_id_in_logs(self):
        """Test that correlation ID is added to log events."""
        correlation_id = "test-correlation-id"
        self.processor.set_correlation_id(correlation_id)
        
        event_dict = {"message": "test"}
        result = self.processor(None, "info", event_dict)
        
        assert result["correlation_id"] == correlation_id
        assert result["message"] == "test"
    
    def test_no_correlation_id(self):
        """Test behavior when no correlation ID is set."""
        event_dict = {"message": "test"}
        result = self.processor(None, "info", event_dict)
        
        assert "correlation_id" not in result
        assert result["message"] == "test"


class TestDecorators:
    """Test cases for logging decorators."""
    
    def setup_method(self):
        """Setup method for each test."""
        LoggingService._instance = None
        LoggingService._initialized = False
    
    def test_log_performance_decorator(self):
        """Test log_performance decorator."""
        @log_performance("test_operation")
        def test_function():
            time.sleep(0.01)
            return "success"
        
        result = test_function()
        assert result == "success"
    
    def test_log_exceptions_decorator(self):
        """Test log_exceptions decorator."""
        @log_exceptions({"component": "test"})
        def test_function():
            raise ValueError("Test exception")
        
        with pytest.raises(ValueError):
            test_function()
    
    def test_combined_decorators(self):
        """Test combining performance and exception decorators."""
        @log_performance("test_operation")
        @log_exceptions({"component": "test"})
        def test_function():
            time.sleep(0.01)
            return "success"
        
        result = test_function()
        assert result == "success"


class TestIntegration:
    """Integration tests for the logging service."""
    
    def setup_method(self):
        """Setup method for each test."""
        LoggingService._instance = None
        LoggingService._initialized = False
    
    def test_full_logging_flow(self):
        """Test complete logging flow."""
        service = LoggingService()
        
        # Set correlation ID
        correlation_id = str(uuid.uuid4())
        service.set_correlation_id(correlation_id)
        
        # Bind context
        logger = service.bind_context(user_id="123", session_id="456")
        
        # Log messages
        logger.info("Test message", order_id="789")
        
        # Test performance tracking
        with service.performance_tracking("test_operation"):
            time.sleep(0.01)
        
        # Test exception logging
        try:
            raise ValueError("Test exception")
        except Exception as e:
            service.log_exception(e, context={"test": "context"})
        
        # All operations should complete without errors
        assert True
    
    def test_concurrent_logging(self):
        """Test concurrent logging operations."""
        service = LoggingService()
        results = []
        
        def log_operation(thread_id):
            correlation_id = str(uuid.uuid4())
            service.set_correlation_id(correlation_id)
            
            logger = service.bind_context(thread_id=thread_id)
            logger.info("Thread message", thread_id=thread_id)
            
            results.append(service.get_correlation_id())
        
        # Create multiple threads
        threads = []
        for i in range(5):
            thread = threading.Thread(target=log_operation, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Each thread should have its own correlation ID
        assert len(results) == 5
        assert len(set(results)) == 5


if __name__ == "__main__":
    pytest.main([__file__]) 