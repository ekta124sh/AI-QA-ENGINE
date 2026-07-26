from backend.ai.models.ai_request import AIRequest
from backend.ai.models.ai_response import AIResponse

from backend.llm.router import LLMRouter


class AIEngine:

    @staticmethod
    def execute(request: AIRequest) -> AIResponse:

        router = LLMRouter()

        try:

            print("=" * 80)
            print(f"AI ENGINE STARTED [{request.task.value.upper()}]")
            print("=" * 80)

            print("\nSending Prompt to LLM...\n")

            # Print only first 2000 chars to avoid huge console output
            print(request.prompt[:2000])

            if len(request.prompt) > 2000:
                print("\n... Prompt Truncated ...\n")

            print("=" * 80)

            response = router.generate(request.prompt)

            print("\nLLM Generation Completed.")

            print("=" * 80)
            print("RAW LLM RESPONSE")
            print("=" * 80)

            if response:
                print(response[:2000])

                if len(response) > 2000:
                    print("\n... Response Truncated ...\n")
            else:
                print("LLM returned an empty response.")

            print("=" * 80)

            return AIResponse(
                success=True,
                content=response,
                model=router.provider.__class__.__name__,
            )

        except Exception as e:

            print("\nAI Engine Error")
            print("=" * 80)
            print(str(e))
            print("=" * 80)

            return AIResponse(
                success=False,
                content="",
                error=str(e),
            )