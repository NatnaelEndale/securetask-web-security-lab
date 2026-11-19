def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy",
        "service": "SecureTask API",
        "version": "1.0.0",
    }

def test_create_task(client):
    payload = {
        "title": "Learn API Integration Testing",
        "description": "Test FastAPI using Pytest and TestClient",
    }

    response = client.post("/api/v1/tasks", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] > 1
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    assert "created_at" in data
    assert "updated_at" in data

def test_create_task_with_invalid_data(client):
    payload = {
        "title": "",
        "description": "Invalid task",
    }

    response = client.post("/api/v1/tasks", json=payload)

    assert response.status_code == 422

def test_get_all_tasks(client):
    # Create two tasks
    client.post(
        "/api/v1/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Build backend APIs",
        },
    )

    client.post(
        "/api/v1/tasks",
        json={
            "title": "Learn Web Security",
            "description": "Study IDOR and authentication",
        },
    )

    # Retrieve all tasks
    response = client.get("/api/v1/tasks")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["title"] == "Learn FastAPI"
    assert data[1]["title"] == "Learn Web Security"

def test_get_task_by_id(client):
    # Create a task
    create_response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Study API Security",
            "description": "Learn access control",
        },
    )

    task_id = create_response.json()["id"]

    # Retrieve the task using its ID
    response = client.get(f"/api/v1/tasks/{task_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Study API Security"
    assert data["description"] == "Learn access control"
    assert data["completed"] is False

def test_update_task(client):
    # Create a task first
    create_response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Build backend APIs",
        },
    )

    task_id = create_response.json()["id"]

    # Update the task's title
    response = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"title": "Learn FastAPI Testing"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Learn FastAPI Testing"

    # Description should remain unchanged
    assert data["description"] == "Build backend APIs"
    assert data["completed"] is False


def test_update_nonexistent_task(client):
    response = client.patch(
        "/api/v1/tasks/999",
        json={"title": "Updated title"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

def test_delete_task(client):
    # Create a task first
    create_response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Learn API Security",
            "description": "Study IDOR and access control",
        },
    )

    task_id = create_response.json()["id"]

    # Delete the task
    response = client.delete(f"/api/v1/tasks/{task_id}")

    assert response.status_code == 204
    assert response.content == b""

    # Verify that the task no longer exists
    get_response = client.get(f"/api/v1/tasks/{task_id}")

    assert get_response.status_code == 404


def test_delete_nonexistent_task(client):
    response = client.delete("/api/v1/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

def test_get_nonexistent_task(client):
    response = client.get("/api/v1/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_get_all_tasks_when_empty(client):
    response = client.get("/api/v1/tasks")

    assert response.status_code == 200
    assert response.json() == []