
from app.repositories.task_repository import TaskRepository


def test_create_task():
    repo = TaskRepository()

    task = repo.create_task(
        title="Learn FastAPI",
        description="Build SecureTask backend",
    )

    assert task.id == 1
    assert task.title == "Learn FastAPI"
    assert task.description == "Build SecureTask backend"
    assert task.completed is False
    assert task.created_at == task.updated_at


def test_get_all_tasks():
    repo = TaskRepository()

    repo.create_task(title="Task 1")
    repo.create_task(title="Task 2")

    tasks = repo.get_all_tasks()

    assert len(tasks) == 2


def test_get_task_by_id():
    repo = TaskRepository()

    created = repo.create_task(title="Test task")
    retrieved = repo.get_task_by_id(created.id)

    assert retrieved == created


def test_update_task():
    repo = TaskRepository()

    task = repo.create_task(title="Original title")

    updated = repo.update_task(
        task.id,
        {"title": "Updated title", "completed": True},
    )

    assert updated is not None
    assert updated.title == "Updated title"
    assert updated.completed is True
    assert updated.updated_at >= task.updated_at


def test_delete_task():
    repo = TaskRepository()

    task = repo.create_task(title="Delete me")

    result = repo.delete_task(task.id)

    assert result is True
    assert repo.get_task_by_id(task.id) is None


def test_delete_nonexistent_task():
    repo = TaskRepository()

    result = repo.delete_task(999)

    assert result is False
