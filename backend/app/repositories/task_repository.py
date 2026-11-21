
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import TaskRecord
from app.models.task_orm import TaskORM


class TaskRepository:
    """Handles database operations for tasks."""

    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def _to_record(task: TaskORM) -> TaskRecord:
        """Convert a database ORM object into a domain record."""

        return TaskRecord(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=task.completed,
            created_at=task.created_at,
            updated_at=task.updated_at,
        )

    def create_task(
        self,
        title: str,
        description: str = "",
    ) -> TaskRecord:

        task = TaskORM(
            title=title,
            description=description,
            completed=False,
        )

        self.session.add(task)
        self.session.flush()
        self.session.refresh(task)

        return self._to_record(task)

    def get_all_tasks(self) -> list[TaskRecord]:

        statement = select(TaskORM).order_by(TaskORM.id)

        tasks = self.session.scalars(statement).all()

        return [
            self._to_record(task)
            for task in tasks
        ]

    def get_task_by_id(self, task_id: int) -> TaskRecord | None:

        task = self.session.get(TaskORM, task_id)

        if task is None:
            return None

        return self._to_record(task)

    def update_task(
        self,
        task_id: int,
        updates: dict,
    ) -> TaskRecord | None:

        task = self.session.get(TaskORM, task_id)

        if task is None:
            return None

        allowed_fields = {
            "title",
            "description",
            "completed",
        }

        if not updates:
            return self._to_record(task)

        if not set(updates).issubset(allowed_fields):
            raise ValueError("Invalid task update fields")

        if any(value is None for value in updates.values()):
            raise ValueError("Task update values cannot be None")

        for field, value in updates.items():
            setattr(task, field, value)

        self.session.flush()
        self.session.refresh(task)

        return self._to_record(task)

    def delete_task(self, task_id: int) -> bool:

        task = self.session.get(TaskORM, task_id)

        if task is None:
            return False

        self.session.delete(task)
        self.session.flush()

        return True
