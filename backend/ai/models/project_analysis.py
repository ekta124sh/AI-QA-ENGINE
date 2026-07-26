from dataclasses import dataclass
from typing import List


@dataclass
class ProjectAnalysis:

    framework: str | None

    database: str | None

    orm: str | None

    models: List[str]

    routers: List[str]

    middlewares: List[str]

    authentication: List[str]