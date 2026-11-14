from fastapi import FastAPI

from app.api.routes import health, task

app = FastAPI(
    title="SecureTask API",
    description="Backend API for the SecureTask application.",
    version="1.0.0"
)

# Register API routes
app.include_router(
    health.router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    task.router,
    prefix="/api/v1",
    tags=["Tasks"],
)
