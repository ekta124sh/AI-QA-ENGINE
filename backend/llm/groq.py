from groq import Groq

from backend.config.settings import settings
from backend.llm.base import BaseLLM
from backend.llm.utils.retry_handler import RetryHandler


class GroqProvider(BaseLLM):
    """
    Groq LLM Provider

    Uses Llama 3.3 70B for deterministic JSON generation.
    """

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate(self, prompt: str) -> str:

        def operation():

            print("=" * 70)
            print("GROQ PROVIDER")
            print("Model : llama-3.3-70b-versatile")
            print("=" * 70)

            completion = self.client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                temperature=0,

                max_tokens=4096,

                top_p=1,

                stream=False,

                messages=[

                    {
                        "role": "system",
                        "content": (
                            "You are a Principal QA Automation Architect.\n\n"

                            "You ONLY generate JSON.\n"

                            "Rules:\n"

                            "1. Return ONLY valid JSON.\n"

                            "2. Never explain anything.\n"

                            "3. Never use markdown.\n"

                            "4. Never wrap JSON inside ```.\n"

                            "5. Never return comments.\n"

                            "6. Never use single quotes.\n"

                            "7. The response MUST start with [\n"

                            "8. The response MUST end with ]\n"

                            "9. Every key must use double quotes.\n"

                            "10. Follow the schema exactly."
                        ),
                    },

                    {
                        "role": "user",
                        "content": prompt,
                    },

                ],
            )

            response = completion.choices[0].message.content

            if response is None:
                raise Exception(
                    "Groq returned an empty response."
                )

            response = response.strip()

            print("\nGenerated Characters :", len(response))
            print("=" * 70)

            return response

        return RetryHandler.execute(operation)