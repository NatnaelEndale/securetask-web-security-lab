
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TaskRecord:
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime
