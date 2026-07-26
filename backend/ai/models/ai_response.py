from dataclasses import dataclass


@dataclass
class AIResponse:

    success: bool

    content: str

    tokens: int = 0

    model: str = ""

    error: str = ""