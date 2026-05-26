from dotenv import load_dotenv
import os

from openai import AzureOpenAI

from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document



load_dotenv()



client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)



embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version="2024-02-15-preview"
)



text = """
Inventory policies ensure stock availability.

Store 20 has the highest weekly sales.

Holiday seasons increase sales significantly.

Retail analytics improves forecasting accuracy.
"""



text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = text_splitter.split_text(text)

docs = [
    Document(page_content=chunk)
    for chunk in chunks
]



vectorstore = FAISS.from_documents(
    docs,
    embeddings
)


retriever = vectorstore.as_retriever()



def ask_rag_question(query: str):

    retrieved_docs = retriever.invoke(query)

    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": "You are a retail document assistant."
            },
            {
                "role": "user",
                "content": f"""
                Context:
                {context}

                Question:
                {query}
                """
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content



if __name__ == "__main__":

    query = input("Ask question: ")

    answer = ask_rag_question(query)

    print("\nRAG Response:\n")

    print(answer)