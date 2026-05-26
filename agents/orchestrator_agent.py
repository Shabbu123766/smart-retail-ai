from agents.rag_document_agent import ask_rag_question
from agents.document_intelligence_agent import analyze_document
from agents.sentiment_agent import analyze_sentiment



# ORCHESTRATOR FUNCTION

def orchestrate_query(query: str):

    query_lower = query.lower()


    
    # ML INSIGHT AGENT

    if (
        "prediction" in query_lower
        or "forecast" in query_lower
        or "future sales" in query_lower
        or "predict" in query_lower
    ):

        return {
            "agent": "ML Insight Agent",
            "response": "ML prediction analysis generated successfully."
        }


    
    # DOCUMENT RAG AGENT

    elif (
        "inventory" in query_lower
        or "policy" in query_lower
        or "document" in query_lower
        or "knowledge" in query_lower
    ):

        rag_response = ask_rag_question(query)

        return {
            "agent": "Document RAG Agent",
            "response": rag_response
        }


    
    # DOCUMENT INTELLIGENCE AGENT

    elif (
        "invoice" in query_lower
        or "receipt" in query_lower
        or "extract text" in query_lower
        or "ocr" in query_lower
    ):

        document_text = analyze_document(
            "documents/sample_invoice.pdf"
        )

        return {
            "agent": "Document Intelligence Agent",
            "response": document_text
        }


    
    # SENTIMENT ANALYSIS AGENT

    elif (
        "sentiment" in query_lower
        or "customer review" in query_lower
        or "feedback" in query_lower
        or "opinion" in query_lower
        or "service" in query_lower
        or "delivery" in query_lower
    ):

        sentiment_result = analyze_sentiment(
            query
        )

        return {
            "agent": "Sentiment Analysis Agent",
            "response": sentiment_result
        }


    
    # RETAIL DATA AGENT

    elif (
        "sales" in query_lower
        or "store" in query_lower
        or "retail" in query_lower
        or "revenue" in query_lower
    ):

        return {
            "agent": "Retail Data Agent",
            "response": "Store 20 has the highest weekly sales."
        }


    
    # DEFAULT RESPONSE

    else:

        return {
            "agent": "Unknown",
            "response": "No matching agent found."
        }



# TERMINAL TESTING

if __name__ == "__main__":

    query = input(
        "Ask your retail question: "
    )

    result = orchestrate_query(query)

    print("\nOrchestrator Result:\n")

    print(result)