from backend.llm.gemini import ask_gemini

response = ask_gemini(
    "Say hello and tell me you are ready to generate software test cases."
)

print(response)