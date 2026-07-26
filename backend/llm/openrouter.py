from openai import OpenAI

from backend.config.settings import settings
from backend.llm.base import BaseLLM


class OpenRouterProvider(BaseLLM):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(self, prompt: str) -> str:

        print("=" * 60)
        print("OPENROUTER PROVIDER")
        print("Using model: openrouter/free")
        print("=" * 60)

        response = self.client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content