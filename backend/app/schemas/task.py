
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Fields accepted when creating a task."""

    title: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=2000)


class TaskUpdate(BaseModel):
    """Fields accepted when updating an existing task."""

    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=2000)
    completed: bool | None = None


class TaskResponse(BaseModel):
    """Fields returned to the API client."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime
