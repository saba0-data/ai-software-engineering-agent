from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_plan() -> None:
    response = client.post(
        "/api/v1/plan",
        json={
            "requirement": "Build a REST API for managing tasks.",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["requirement"] == "Build a REST API for managing tasks."
    assert len(data["plan"]) > 0
    assert len(data["files"]) > 0

    assert len(data["generated_code"]) > 0
    assert "app/models.py" in data["generated_code"]

    assert len(data["test_cases"]) > 0
    assert "test_task_model_creation" in data["test_cases"]

    assert data["errors"] == []