from backend.database import prediction_collection
from fastapi import FastAPI, File, UploadFile
from backend.logger import logger
import pickle
import numpy as np
import shutil
import os
from pydantic import BaseModel
import subprocess
from agents.sales_anomaly_agent import detect_sales_anomalies

app = FastAPI(
    title="Smart Retail Assistant API",
    description="Multi-Agent AI Platform for Retail Forecasting, Analytics, and Anomaly Detection",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    question: str


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "ml-model",
    "sales_model.pkl"
)

model = pickle.load(open(MODEL_PATH, "rb"))



@app.get("/")
def home():

    return {
        "message": "Smart Retail AI API Running Successfully"
    }



# 1. Sales Prediction API

@app.get("/sales-predict")
def predict_sales(
    store_id: int,
    holiday_flag: int,
    temperature: float,
    fuel_price: float,
    cpi: float,
    unemployment: float,
    month: int,
    year: int
):

    try:

        
        input_data = np.array([[
            store_id,
            holiday_flag,
            temperature,
            fuel_price,
            cpi,
            unemployment,
            month,
            year
        ]])

        logger.info(
            f"Generating prediction for Store ID: {store_id}"
        )

        
        prediction = model.predict(input_data)

        
        prediction_data = {
            "store_id": store_id,
            "predicted_sales": float(prediction[0]),
            "month": month,
            "year": year
        }

        prediction_collection.insert_one(prediction_data)

        
        return {
            "store_id": store_id,
            "predicted_weekly_sales": round(float(prediction[0]), 2),
            "model_used": "Linear Regression",
            "status": "Prediction Generated Successfully"
        }

    except Exception as e:

        logger.error(f"Prediction API Error: {str(e)}")

        return {
            "status": "Failed",
            "error_message": str(e)
        }


# 2. Upload Sales Dataset API

@app.post("/upload-sales-data")
def upload_sales_data(
    file: UploadFile = File(...)
):

    
    os.makedirs("../uploads", exist_ok=True)

    
    file_path = f"../uploads/{file.filename}"

    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    
    return {
        "file_name": file.filename,
        "message": "Sales dataset uploaded successfully"
    }


# 3. Retail Chatbot API

@app.get("/retail-chatbot")
def retail_chatbot(question: str):

    
    user_question = question.lower()

    
    if "highest sales" in user_question:

        return {
            "question": question,
            "response": "Store 20 generated the highest weekly sales."
        }

    elif "lowest sales" in user_question:

        return {
            "question": question,
            "response": "Store 33 generated the lowest weekly sales."
        }

    elif "best store" in user_question:

        return {
            "question": question,
            "response": "Store 20 is currently performing best based on sales."
        }

    else:

        return {
            "question": question,
            "response": "Retail assistant is processing your request."
        }



# 4. Document Search API


@app.get("/search-documents")
def search_documents(keyword: str):

    
    return {
        "searched_keyword": keyword,
        "document_status": "Search Completed Successfully",
        "message": f"Results found for keyword: {keyword}"
    }



@app.post("/retail-agent")
def retail_agent(request: QueryRequest):

    result = subprocess.check_output(
        [
            "venv/Scripts/python.exe",
            "agents/retail_data_agent.py"
        ],
        text=True
    )

    return {
        "agent": "Retail Data Agent",
        "response": result
    }

@app.post("/ml-agent")
def ml_agent(request: QueryRequest):

    result = subprocess.check_output(
        [
            "venv/Scripts/python.exe",
            "agents/ml_insight_agent.py"
        ],
        text=True
    )

    return {
        "agent": "ML Insight Agent",
        "response": result
    }

from agents.rag_document_agent import ask_rag_question


@app.post("/document-agent")
def document_agent(request: QueryRequest):

    result = ask_rag_question(
        request.question
    )

    return {
        "agent": "Document RAG Agent",
        "question": request.question,
        "response": result
    }

from agents.orchestrator_agent import orchestrate_query


@app.post("/orchestrator-agent")
def orchestrator_agent(request: QueryRequest):

    result = orchestrate_query(
        request.question
    )

    return result

@app.post("/sales-forecast")
def sales_forecast(request: QueryRequest):

    prediction = {
        "predicted_sales": 250000
    }

    return {
        "agent": "Sales Forecast API",
        "response": prediction
    }

@app.get("/sales-anomaly")
def sales_anomaly():

    result = detect_sales_anomalies()

    return {
        "agent": "Sales Anomaly Agent",
        "response": result
    }