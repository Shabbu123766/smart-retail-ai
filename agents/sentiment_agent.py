from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

import os



# LOAD ENV VARIABLES


load_dotenv()



# AZURE CONFIG

endpoint = os.getenv(
    "TEXT_ANALYTICS_ENDPOINT"
)

key = os.getenv(
    "TEXT_ANALYTICS_KEY"
)



# CREATE CLIENT

text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)



# MAIN SENTIMENT FUNCTION

def analyze_sentiment(text: str):

    response = text_analytics_client.analyze_sentiment(
        documents=[text]
    )[0]


    result = {
        "sentiment": response.sentiment,
        "positive_score": response.confidence_scores.positive,
        "neutral_score": response.confidence_scores.neutral,
        "negative_score": response.confidence_scores.negative
    }


    return result


# TERMINAL TESTING

if __name__ == "__main__":

    customer_review = """
    The retail service was excellent and delivery was fast.
    """

    result = analyze_sentiment(
        customer_review
    )

    print("\nSentiment Analysis Result:\n")

    print(result)