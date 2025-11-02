# Version: 1.0
# Developed by: Márcio Rodrigo
import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    # Main Streamlit UI: lets the user upload an image and triggers analysis
    st.title("File Upload - Azure Fake Docs")
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Upload the selected file to Azure Blob Storage
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"File {fileName} successfully uploaded to Azure Blob Storage")
            # Call Document Intelligence to analyze the uploaded image URL
            with st.spinner("Analyzing credit card with Document Intelligence..."):
                credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Error uploading file {fileName} to Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    # Show the uploaded image and the result of the analysis
    st.image(blob_url, caption="Uploaded image", use_column_width=True)
    st.write("Validation result:")
    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color: green;'>Valid Credit Card</h1>", unsafe_allow_html=True)
        st.write(f"Cardholder Name: {credit_card_info['card_name']}")
        st.write(f"Issuing Bank: {credit_card_info['bank_name']}")
        st.write(f"Expiration Date: {credit_card_info['expiry_date']}")
    else:
        st.markdown("<h1 style='color: red;'>Invalid Credit Card</h1>", unsafe_allow_html=True)
        st.write("This is not a valid credit card.")

if __name__ == "__main__":
    configure_interface()