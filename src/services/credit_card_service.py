# Version: 1.0
# Developed by: Márcio Rodrigo
from typing import Optional, Dict

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

from utils.Config import Config


def analyze_credit_card(card_url: str) -> Optional[Dict[str, str]]:
    """Analyze a credit card image URL using Azure Document Intelligence.

    Returns a dict with keys like 'card_name', 'bank_name', 'expiry_date' if detected,
    otherwise returns None.
    """
    try:
        # Authenticate using the subscription key
        credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
        # Create a client pointing to your Document Intelligence endpoint
        client = DocumentIntelligenceClient(endpoint=Config.ENDPOINT, credential=credential)

        # Start analysis with the prebuilt model for credit cards
        poller = client.begin_analyze_document(
            model_id="prebuilt:creditCard",
            analyze_request=AnalyzeDocumentRequest(url_source=card_url),
        )
        # Wait for the analysis to complete
        result = poller.result()

        info: Dict[str, str] = {}
        # Extract common fields if present
        try:
            d = result.documents[0]
            if d.fields:
                if "CardHolderName" in d.fields and d.fields["CardHolderName"].value is not None:
                    info["card_name"] = str(d.fields["CardHolderName"].value)
                if "IssuingBank" in d.fields and d.fields["IssuingBank"].value is not None:
                    info["bank_name"] = str(d.fields["IssuingBank"].value)
                if "ExpirationDate" in d.fields and d.fields["ExpirationDate"].value is not None:
                    info["expiry_date"] = str(d.fields["ExpirationDate"].value)
        except Exception:
            pass

        return info if info else None
    except Exception:
        return None
