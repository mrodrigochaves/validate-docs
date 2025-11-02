# Validate Docs (Streamlit)

Simple Streamlit app that uploads an image to Azure Blob Storage and analyzes it with Azure Document Intelligence (prebuilt:creditCard). 

Developed by Marcio Rodrigo — v1.0

## Prerequisites
- Python 3.11 (recommended)
- Azure Storage Account (connection string)
- Azure AI Document Intelligence resource (endpoint + key)

## Setup
1) Clone this repository and open a terminal in the project root.
2) Create and activate a virtual environment (Windows PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3) Install dependencies:
```powershell
python -m pip install -r src\requirements.txt
```
4) Create a `.env` file in the project root (or copy from `.envexample`) and fill with your values:
```
ENDPOINT=https://<your-di-resource>.cognitiveservices.azure.com/
SUBSCRIPTION_KEY=<your-di-key>
AZURE_STORAGE_CONNECTION_STRING=<your-storage-connection-string>
CONTAINER_NAME=<your-container-name>
```

## Run
Start the Streamlit app:
```powershell
python -m streamlit run src\app.py
```
Then open the local URL shown in the terminal (usually http://localhost:8501).

## Project Structure
- `src/app.py` — Streamlit UI and main flow (upload -> analyze -> display).
- `src/services/blob_service.py` — Upload helper to Azure Blob (returns blob URL).
- `src/services/credit_card_service.py` — Calls Azure Document Intelligence.
- `src/utils/Config.py` — Loads configuration from environment variables.
- `src/requirements.txt` — Python dependencies.
- `.envexample` — Example env file with required keys.

## Notes
- The blob container is created with public access to blobs to enable direct image display in Streamlit.
- The analysis uses the `prebuilt:creditCard` model; results depend on image quality and content.
