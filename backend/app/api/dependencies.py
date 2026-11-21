from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    """Provide a task service using the request's database session."""

    repository = TaskRepository(db)

    return TaskService(repository)