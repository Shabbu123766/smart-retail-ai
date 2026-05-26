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


response = client.chat.completions.create(

    model=deployment_name,

    messages=[

        {
            "role": "system",

            "content": """

            You are a Retail Data Analyst Agent.

            Responsibilities:
            - Analyze retail sales
            - Identify top-performing stores
            - Explain sales trends
            - Provide business insights

            Guidelines:
            - Keep responses short and professional
            - Use only provided retail insights

            """
        },

        {
            "role": "user",

            "content": """

            Retail Sales Insights:

            - Store 20 has highest sales
            - February and December show strong demand
            - Average weekly sales are around 1.2 million

            Question:
            Which store has highest sales?

            """
        }
    ]
)


print("\nRetail Agent Response:\n")

print(response.choices[0].message.content)