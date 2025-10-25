import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.database.database import Base
from src.infrastructure.redis.redis_client import RedisClient
from order.src.infrastructure.di.dependency_injection_container import container
from unittest.mock import AsyncMock

# Database setup for tests
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_engine():
    engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost:5432/test_order_service")
    yield engine
    await engine.dispose()

@pytest.fixture(scope="session")
async def test_session_factory(test_engine):
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    Session = sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)
    yield Session
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def db_session(test_session_factory):
    async with test_session_factory() as session:
        yield session
        await session.rollback()

# Redis mock
@pytest.fixture
async def redis_client(mocker):
    redis_mock = AsyncMock(spec=RedisClient)
    redis_mock.client.pipeline.return_value.__aenter__.return_value = AsyncMock()
    redis_mock.client.pipeline.return_value.__aexit__.return_value = None
    yield redis_mock

# Kafka producer mock
@pytest.fixture
def kafka_producer(mocker):
    kafka_mock = AsyncMock()
    kafka_mock.start = AsyncMock()
    kafka_mock.stop = AsyncMock()
    kafka_mock.publish_event = AsyncMock()
    return kafka_mock

# gRPC client mocks
@pytest.fixture
def course_service_client(mocker):
    course_mock = AsyncMock()
    course_mock.get_course = AsyncMock(return_value={"course_id": "course1", "price": 100.0})
    return course_mock

@pytest.fixture
def session_service_client(mocker):
    session_mock = AsyncMock()
    session_mock.get_session = AsyncMock(return_value={"session_id": "session1", "price": 50.0, "max_slots": 10})
    session_mock.get_available_slots = AsyncMock(return_value=5)
    return session_mock

@pytest.fixture
def user_service_client(mocker):
    user_mock = AsyncMock()
    user_mock.verify_user = AsyncMock(return_value={"user_id": "user1", "role": "STUDENT"})
    return user_mock
