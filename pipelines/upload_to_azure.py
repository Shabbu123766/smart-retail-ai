import os

from dotenv import load_dotenv

from azure.storage.blob import BlobServiceClient



load_dotenv()



connection_string = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)



blob_service_client = BlobServiceClient.from_connection_string(
    connection_string
)



container_name = "curated-data"



local_file_path = "data/curated/curated_walmart.parquet"



blob_name = "curated_walmart.parquet"



blob_client = blob_service_client.get_blob_client(
    container=container_name,
    blob=blob_name
)



with open(local_file_path, "rb") as data:

    blob_client.upload_blob(
        data,
        overwrite=True
    )


print("File uploaded to Azure Blob Storage successfully!")