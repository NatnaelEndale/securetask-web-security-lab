
from fastapi import APIRouter, Depends, status, HTTPException, Response

from app.api.dependencies import get_task_service
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService, TaskNotFoundError


router = APIRouter()


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task_data: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return service.create_task(
        title=task_data.title,
        description=task_data.description,
    )


@router.get(
    "/tasks",
    response_model=list[TaskResponse]
)
def get_all_tasks(
    service: TaskService = Depends(get_task_service),
):
    return service.get_all_tasks()

@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    try:
        return service.get_task(task_id)

    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

@router.patch(
    "/tasks/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    updates = task_data.model_dump(exclude_unset=True)

    try:
        return service.update_task(task_id, updates)

    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        )

@router.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    try:
        service.delete_task(task_id)

    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)