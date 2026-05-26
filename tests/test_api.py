import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.main import app
from fastapi.testclient import TestClient



client = TestClient(app)



def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Smart Retail AI API Running Successfully"
    }



def test_sales_prediction():

    response = client.get(
        "/sales-predict?store_id=1&holiday_flag=0&temperature=42&fuel_price=3&cpi=211&unemployment=8&month=5&year=2012"
    )

    assert response.status_code == 200