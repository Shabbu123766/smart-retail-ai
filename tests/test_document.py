from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_document_agent():

    response = client.post(
        "/document-agent",
        json={
            "question": "What are inventory policies?"
        }
    )

    assert response.status_code == 200