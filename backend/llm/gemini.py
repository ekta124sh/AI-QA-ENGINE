from google import genai

from backend.config.settings import settings
from backend.llm.base import BaseLLM
from backend.llm.utils.retry_handler import RetryHandler


class GeminiProvider(BaseLLM):

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        def operation():

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={
                    "temperature": 0.2,
                    "max_output_tokens": 4096,
                },
            )

            return response.text

        return RetryHandler.execute(
            operation=operation,
            max_retries=3,
            wait_seconds=20,
        )