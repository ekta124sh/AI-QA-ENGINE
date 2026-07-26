from backend.config.settings import settings
from backend.llm.factory import get_llm


class LLMRouter:
    """
    Intelligent router with provider fallback.
    """

    def __init__(self):

        # Use ONLY the configured provider
        self.providers = [
            settings.LLM_PROVIDER.lower(),
        ]

    def generate(self, prompt: str) -> str:

        last_error = None

        for provider_name in self.providers:

            try:

                print(f"\nUsing Provider: {provider_name}")

                provider = get_llm(provider_name)

                self.provider = provider

                return provider.generate(prompt)

            except Exception as ex:

                print(f"Provider {provider_name} failed.")
                print(ex)
                last_error = ex

        raise last_error