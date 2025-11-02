# Version: 1.0
# Developed by: Márcio Rodrigo
import os
from dotenv import load_dotenv

# Load environment variables from .env file at project root
load_dotenv()

class Config:
    """Centralized configuration loaded from environment variables.

    Make sure your .env contains valid values for the keys below.
    """
    # Azure Document Intelligence endpoint (e.g., https://<resource>.cognitiveservices.azure.com/)
    ENDPOINT = os.getenv("ENDPOINT")
    # Azure Document Intelligence subscription key
    SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
    # Azure Storage connection string (used to upload files to Blob Storage)
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    # Target container name where files will be uploaded
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")


if __name__ == "__main__":
    # Quick check when running this file directly
    print(Config.ENDPOINT)