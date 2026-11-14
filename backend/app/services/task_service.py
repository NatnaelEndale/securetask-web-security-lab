
from app.repositories.task_repository import TaskRepository
from app.models.task import TaskRecord


class TaskNotFoundError(Exception):
    """Raised when a requested task does not exist."""


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(
        self,
        title: str,
        description: str = "",
    ) -> TaskRecord:
        return self.repository.create_task(
            title=title,
            description=description,
        )

    def get_all_tasks(self) -> list[TaskRecord]:
        return self.repository.get_all_tasks()

    def get_task(self, task_id: int) -> TaskRecord:
        task = self.repository.get_task_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(
                f"Task with ID {task_id} was not found"
            )

        return task

    def update_task(
        self,
        task_id: int,
        updates: dict,
    ) -> TaskRecord:
        task = self.repository.update_task(task_id, updates)

        if task is None:
            raise TaskNotFoundError(
                f"Task with ID {task_id} was not found"
            )

        return task

    def delete_task(self, task_id: int) -> None:
        deleted = self.repository.delete_task(task_id)

        if not deleted:
            raise TaskNotFoundError(
                f"Task with ID {task_id} was not found"
            )
