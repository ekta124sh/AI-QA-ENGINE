from backend.analyzers.repository_analyzer import RepositoryAnalyzer
from backend.context.repository_context import RepositoryContext
from backend.services.git_service import GitService


repo = GitService.clone_repository(
    "https://github.com/fastapi/fastapi"
)

analysis = RepositoryAnalyzer.analyze(repo)

context = RepositoryContext.build(
    analysis,
    current_file="main.py",
)

print()
print("=" * 60)
print("REPOSITORY CONTEXT")
print("=" * 60)

for key, value in context.items():

    if key == "endpoints":
        print(f"{key}: {len(value)} endpoints")

        for endpoint in value[:10]:
            print("   ", endpoint)

    else:
        print(f"{key}: {value}")