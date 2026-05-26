from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

import os




load_dotenv()



# AZURE CONFIG


endpoint = os.getenv(
    "DOCUMENT_INTELLIGENCE_ENDPOINT"
)

key = os.getenv(
    "DOCUMENT_INTELLIGENCE_KEY"
)



# CREATE CLIENT

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)



# MAIN FUNCTION

def analyze_document(file_path: str):

    with open(file_path, "rb") as f:

        poller = document_analysis_client.begin_analyze_document(
            "prebuilt-document",
            document=f
        )

        result = poller.result()


    extracted_text = ""


    for page in result.pages:

        for line in page.lines:

            extracted_text += line.content + "\n"


    return extracted_text



# TERMINAL TESTING

if __name__ == "__main__":

    result = analyze_document(
        "documents/Sample_invoice.pdf"
    )

    print("\nExtracted Document Text:\n")

    print(result)