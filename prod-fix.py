import requests
import logging
import time

# Enable logging
logging.basicConfig(level=logging.INFO)

# External API that we depend on
EXTERNAL_API_URL = "https://api.example.com/data"

def fetch_data():
    """
    Fetches data from an external API. Implements a temporary workaround
    to handle intermittent failures.
    
    Returns:
        dict: The API response or a fallback response in case of failure.
    """
    try:
        response = requests.get(EXTERNAL_API_URL, timeout=3)
        response.raise_for_status()  # Raise an error for non-2xx responses
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed - {e}")
        return {"status": "error", "message": "Data unavailable, using fallback."}

# Simulating multiple requests
if __name__ == "__main__":
    for _ in range(3):
        data = fetch_data()
        print(data)
        time.sleep(2)  # Simulate time delay between requests
