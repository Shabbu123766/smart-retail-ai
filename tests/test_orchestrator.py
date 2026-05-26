from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_orchestrator():

    response = client.post(
        "/orchestrator-agent",
        json={
            "question": "Predict future sales"
        }
    )

    assert response.status_code == 200