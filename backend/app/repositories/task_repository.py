
from dataclasses import replace
from datetime import datetime, timezone

from app.models.task import TaskRecord


class TaskRepository:
    def __init__(self):
        self._tasks: dict[int, TaskRecord] = {}
        self._next_id = 1

    def create_task(
        self,
        title: str,
        description: str = "",
    ) -> TaskRecord:

        now = datetime.now(timezone.utc)

        task = TaskRecord(
            id=self._next_id,
            title=title,
            description=description,
            completed=False,
            created_at=now,
            updated_at=now,
        )

        self._tasks[task.id] = task
        self._next_id += 1

        return task

    def get_all_tasks(self) -> list[TaskRecord]:
        return sorted(
            self._tasks.values(),
            key=lambda task: task.id,
        )

    def get_task_by_id(self, task_id: int) -> TaskRecord | None:
        return self._tasks.get(task_id)

    def update_task(
        self,
        task_id: int,
        updates: dict,
    ) -> TaskRecord | None:

        task = self._tasks.get(task_id)

        if task is None:
            return None

        allowed_fields = {
            "title",
            "description",
            "completed",
        }

        if not updates:
            return task

        if not set(updates).issubset(allowed_fields):
            raise ValueError("Invalid task update fields")

        if any(value is None for value in updates.values()):
            raise ValueError("Task update values cannot be None")

        updated_task = replace(
            task,
            **updates,
            updated_at=datetime.now(timezone.utc),
        )

        self._tasks[task_id] = updated_task

        return updated_task

    def delete_task(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True
        