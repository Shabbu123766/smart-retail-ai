import os

from dotenv import load_dotenv
from openai import AzureOpenAI



load_dotenv()



api_key = os.getenv("AZURE_OPENAI_API_KEY")

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")



client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-02-15-preview",
    azure_endpoint=endpoint
)



predicted_sales = 1109829.07



response = client.chat.completions.create(

    model=deployment_name,

    messages=[

        {
            "role": "system",

            "content": """

            You are an ML Forecasting Expert Agent.

            Responsibilities:
            - Explain ML predictions
            - Interpret forecasting results
            - Provide retail business insights

            Guidelines:
            - Explain clearly
            - Keep answers professional
            - Focus on business impact

            """
        },

        {
            "role": "user",

            "content": f"""

            Retail ML Prediction:

            Predicted Weekly Sales: {predicted_sales}

            Features used:
            - Store ID
            - Temperature
            - Fuel Price
            - CPI
            - Unemployment
            - Month
            - Year
            - Holiday Flag

            Explain this prediction.

            """
        }
    ]
)


print("\nML Insight Agent Response:\n")

print(response.choices[0].message.content)