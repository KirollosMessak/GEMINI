import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

api_key = os.getenv("GOOGLE_API_KEY")
print("API Key:", api_key)  # Debugging step
