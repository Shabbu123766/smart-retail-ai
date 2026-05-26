from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_retail_agent():

    response = client.post(
        "/retail-agent",
        json={
            "question": "Which store has highest sales?"
        }
    )

    assert response.status_code == 200