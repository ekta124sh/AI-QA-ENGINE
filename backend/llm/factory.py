from backend.config.settings import settings

from backend.llm.groq import GroqProvider
from backend.llm.openrouter import OpenRouterProvider


def get_llm(provider=None):

    provider = (provider or settings.LLM_PROVIDER).lower()

    providers = {

        "groq": GroqProvider,

        "openrouter": OpenRouterProvider,

    }

    if provider not in providers:

        raise ValueError(
            f"Unsupported Provider: {provider}"
        )

    return providers[provider]()