# app.py
import streamlit as st
import base64
from gemini_ocr_utils import get_gemini_ocr_text # Import the function

st.set_page_config(page_title="Gemini OCR for Invoices/Receipts", layout="centered")

st.title("📄 Gemini OCR for Invoices & Receipts")
st.markdown("Upload an image of an invoice or receipt, and I'll extract the text using Google Gemini.")

# --- API Key Input (Optional, for local testing) ---
# If you're deploying, use Streamlit Secrets for better security.
# api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")
# if api_key:
#     os.environ["GEMINI_API_KEY"] = api_key # Set environment variable for the script

uploaded_file = st.file_uploader("Choose an image file (JPG, PNG)", type=["jpg", "jpeg", "png"])

extracted_text = ""

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width =True)
    st.write("")
    st.info("Processing image...")

    # Read image as bytes and convert to base64
    bytes_data = uploaded_file.getvalue()
    base64_encoded_image = base64.b64encode(bytes_data).decode('utf-8')

    # Call the Gemini OCR function
    with st.spinner("Extracting text with Gemini..."):
        extracted_text = get_gemini_ocr_text(
            base64_encoded_image,
            "Extract all text and key information like total amount, date, and line items from this invoice or receipt. Present it clearly."
        )

    st.success("Text extraction complete!")

    st.subheader("Extracted Text:")
    st.text_area("OCR Result", extracted_text, height=300)

    st.markdown("---")
    st.markdown("### Tips:")
    st.markdown("- For better results, ensure the image is clear and well-lit.")
    st.markdown("- You can refine the prompt in the `get_gemini_ocr_text` function for more specific extraction (e.g., 'Extract only the total amount').")

else:
    st.info("Please upload an image to get started.")