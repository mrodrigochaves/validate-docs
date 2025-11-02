import streamlit as st
from azure.storage.blob import BlobServiceClient, PublicAccess
from utils.Config import Config


def upload_blob(file, file_name):
    """Upload a file-like object to Azure Blob Storage and return the blob URL."""
    try:
        # Create clients from connection string and container name
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(Config.CONTAINER_NAME)
        try:
            # Ensure container exists and is publicly accessible for blobs (so we can display the image URL)
            container_client.create_container(public_access=PublicAccess.Blob)
        except Exception:
            pass
        # Get a blob client for the target file name
        blob_client = container_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        # Read bytes from Streamlit UploadedFile or raw bytes
        data = file.getvalue() if hasattr(file, "getvalue") else file
        # Upload with overwrite enabled to simplify development
        blob_client.upload_blob(data, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Error uploading file to Azure Blob Storage: {ex}")
        return None
