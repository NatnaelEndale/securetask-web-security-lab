import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api.dependencies import get_task_service
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


@pytest.fixture
def client():
    # Create fresh test dependencies
    test_repository = TaskRepository()
    test_service = TaskService(test_repository)

    # Preserve existing overrides
    original_overrides = app.dependency_overrides.copy()

    # Replace the production service with our test service
    app.dependency_overrides[get_task_service] = lambda: test_service

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        # Restore the original dependency configuration
        app.dependency_overrides.clear()
        app.dependency_overrides.update(original_overrides)