
import pytest

from app.repositories.task_repository import TaskRepository
from app.services.task_service import (
    TaskService,
    TaskNotFoundError,
)


@pytest.fixture
def service():
    repository = TaskRepository()
    return TaskService(repository)


def test_create_task(service):
    task = service.create_task(
        title="Learn FastAPI",
        description="Build SecureTask backend",
    )

    assert task.id == 1
    assert task.title == "Learn FastAPI"


def test_get_all_tasks(service):
    service.create_task(title="Task 1")
    service.create_task(title="Task 2")

    tasks = service.get_all_tasks()

    assert len(tasks) == 2


def test_get_task(service):
    created = service.create_task(title="Test task")

    retrieved = service.get_task(created.id)

    assert retrieved == created


def test_get_nonexistent_task(service):
    with pytest.raises(TaskNotFoundError):
        service.get_task(999)


def test_update_task(service):
    task = service.create_task(title="Original title")

    updated = service.update_task(
        task.id,
        {"title": "Updated title"},
    )

    assert updated.title == "Updated title"


def test_update_nonexistent_task(service):
    with pytest.raises(TaskNotFoundError):
        service.update_task(999, {"title": "Updated title"})


def test_delete_task(service):
    task = service.create_task(title="Delete me")

    service.delete_task(task.id)

    with pytest.raises(TaskNotFoundError):
        service.get_task(task.id)


def test_delete_nonexistent_task(service):
    with pytest.raises(TaskNotFoundError):
        service.delete_task(999)
