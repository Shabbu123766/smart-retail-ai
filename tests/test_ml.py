from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_ml_agent():

    response = client.post(
        "/ml-agent",
        json={
            "question": "Predict future sales"
        }
    )

    assert response.status_code == 200