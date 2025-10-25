import pytest
from src.application.services.saga.saga_orchestrator import SagaOrchestrator, SagaStep
from unittest.mock import AsyncMock
import logging

class MockStep(SagaStep):
    async def execute(self, context):
        context["executed"] = True

    async def compensate(self, context):
        context["compensated"] = True

@pytest.mark.asyncio
async def test_saga_orchestrator_success():
    # Arrange
    logger = logging.getLogger("test")
    step = MockStep()
    saga = SagaOrchestrator(steps=[step], logger=logger)
    context = {}

    # Act
    await saga.execute()

    # Assert
    assert context.get("executed") is True
    assert "compensated" not in context

@pytest.mark.asyncio
async def test_saga_orchestrator_failure():
    # Arrange
    logger = logging.getLogger("test")
    failing_step = AsyncMock()
    failing_step.execute.side_effect = ValueError("Step failed")
    failing_step.compensate = AsyncMock()
    saga = SagaOrchestrator(steps=[failing_step], logger=logger)
    context = {}

    # Act & Assert
    with pytest.raises(ValueError, match="Step failed"):
        await saga.execute()
    failing_step.compensate.assert_called_once()