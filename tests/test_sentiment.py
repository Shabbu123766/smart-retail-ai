from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_sentiment():

    response = client.post(
        "/orchestrator-agent",
        json={
            "question": "The customer service was excellent"
        }
    )

    assert response.status_code == 200