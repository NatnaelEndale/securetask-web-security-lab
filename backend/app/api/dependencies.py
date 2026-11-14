
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


# Create one shared repository instance.
task_repository = TaskRepository()

# Inject the shared repository into the service.
task_service = TaskService(task_repository)


def get_task_service() -> TaskService:
    """Provide the shared task service to API routes."""
    return task_service
