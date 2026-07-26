import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("\nAvailable Models:\n")

for model in client.models.list():
    print(model.name)