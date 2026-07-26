from dataclasses import dataclass

from backend.ai.types.ai_task import AITask


@dataclass
class AIRequest:

    task: AITask

    prompt: str

    metadata: dict | None = None