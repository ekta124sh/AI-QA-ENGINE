import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

test_models = [
    "gemini-flash-latest",
    "gemini-pro-latest",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
]

for model in test_models:
    print(f"\nTesting {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Reply with only OK"
        )

        print("SUCCESS")
        print(response.text)

    except Exception as e:
        print("FAILED")
        print(e)