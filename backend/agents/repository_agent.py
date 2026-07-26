from backend.ai.analyzers.project_analyzer import ProjectAnalyzer
from backend.ai.analyzers.repository_analyzer import RepositoryAnalyzer

from backend.ai.builders.project_context import ProjectContext
from backend.ai.builders.context_builder import ContextBuilder


class RepositoryAgent:
    """
    Builds a complete AI context for a repository.
    """

    @staticmethod
    def analyze(repo_path: str):

        project_info = ProjectAnalyzer.analyze(repo_path)

        project_context = ProjectContext.build(
            project_info
        )

        routes = RepositoryAnalyzer.find_routes(
            repo_path
        )

        repository_context = ContextBuilder.build(
            routes
        )

        return {
            "project_info": project_info,
            "project_context": project_context,
            "routes": routes,
            "repository_context": repository_context,
        }