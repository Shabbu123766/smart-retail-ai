from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_document_intelligence():

    response = client.post(
        "/orchestrator-agent",
        json={
            "question": "Extract text from invoice"
        }
    )

    assert response.status_code == 200