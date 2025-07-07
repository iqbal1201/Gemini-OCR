# Gemini OCR for Invoices and Receipts

This project demonstrates how to use the Google Gemini API to perform Optical Character Recognition (OCR) on images of invoices and receipts, extracting valuable text and key information. The core logic is implemented in Python, designed to be easily integrated into a user interface, such as a Streamlit application.

## Features

* **Image to Text:** Converts text from image files (JPG, PNG) into machine-readable text.

* **Key Information Extraction:** Prompts the Gemini model to specifically identify and extract details like total amounts, dates, and line items from financial documents.

* **Error Handling:** Includes basic error handling for API requests.

## Project Structure

The project consists of two main parts:

1. **`gemini_ocr_utils.py`**: Contains the Python function `get_gemini_ocr_text` which handles the communication with the Gemini API for OCR.

2. **`app.py` (Conceptual Streamlit App)**: A conceptual Streamlit application that provides a user interface for uploading images and displaying the extracted text. (Note: The Streamlit code is provided conceptually and needs to be set up in your local environment.)

## Setup and Installation

To run this project, you'll need Python 3.7+ and the following libraries:

1. **Clone the repository (or create the files):**
   If you have a repository, clone it. Otherwise, create the `gemini_ocr_utils.py` file with the provided Python code and an `app.py` file with the conceptual Streamlit code.

2. **Install Python dependencies:**
```bash
pip install streamlit request python-dotenv
```

3. **Obtain a Google Gemini API Key:**
   - Go to Google AI Studio.
   - Create a new project or select an existing one.
   - Generate an API key.
  
4. **Create .env file:**
   ```bash
   GEMINI_API_KEY=xxxxxxxxxxxxxxx
   ```
5. **Run Streamlit script**
   ```bash
   strealimt run main.py
   ```
6. Result
   
   
