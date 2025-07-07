import base64
import json
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def get_gemini_ocr_text(base64_image_data: str, prompt: str = "Extract all text from this image.") -> str:
    """
    Uses the Gemini API to perform OCR on a base64 encoded image.

    Args:
        base64_image_data: The base64 encoded string of the image.
        prompt: The prompt to send to the Gemini model for text extraction.

    Returns:
        The extracted text from the image, or an error message if the API call fails.
    """
    # Replace with your actual API key or leave empty if running in a Canvas environment
    # where __api_key__ is provided.
    api_key = os.getenv("GEMINI_API_KEY", "") # You can set this as an environment variable or hardcode it for testing.

    if not api_key:
        print("Warning: GEMINI_API_KEY not found. Please set it or provide it in the code.")
        print("For Canvas environment, the API key is automatically provided.")
        # In a real Streamlit app, you might prompt the user for the key or use st.secrets

    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt},
                    {
                        "inlineData": {
                            "mimeType": "image/jpeg", # Adjust mimeType if your image is PNG, etc.
                            "data": base64_image_data
                        }
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        result = response.json()

        if result.get("candidates") and result["candidates"][0].get("content") and result["candidates"][0]["content"].get("parts"):
            extracted_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return extracted_text
        else:
            return f"No text found or unexpected API response structure: {result}"

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - Response: {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred during the API request: {req_err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Example Usage (replace with your actual image data) ---
if __name__ == "__main__":
    # In a real Streamlit app, you would get this from st.file_uploader
    # For demonstration, let's use a dummy base64 string or a function to read a local image.
    # IMPORTANT: Replace this with actual base64 data of an invoice/receipt image.
    # You can convert an image to base64 using online tools or a Python script:
    # with open("path/to/your/image.jpg", "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    # dummy_base64_image = "YOUR_BASE64_ENCODED_IMAGE_STRING_HERE"
    # For a placeholder, you can use a very small, simple base64 encoded image (e.g., a tiny white dot)
    # or just leave it as a comment and explain how to get it.
    # Let's provide a placeholder and instruct the user.

    # Example: A tiny base64 encoded image (a 1x1 white pixel)
    # You MUST replace this with a real invoice/receipt image's base64 data for actual OCR.
    dummy_base64_image = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="

    if dummy_base64_image == "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=":
        print("Please replace 'dummy_base64_image' with the actual base64 encoded data of your invoice/receipt image.")
        print("You can use a tool like https://www.base64-image.de/ or a Python script to convert your image to base64.")
    else:
        print("Performing OCR...")
        extracted_text = get_gemini_ocr_text(dummy_base64_image, "Extract all text and key information like total amount, date, and items from this invoice/receipt.")
        print("\n--- Extracted Text ---")
        print(extracted_text)

