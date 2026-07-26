from pprint import pprint

from backend.analyzers.repository_analyzer import RepositoryAnalyzer


repo = "repositories/fastapi"

result = RepositoryAnalyzer.analyze(repo)

print("\n" + "=" * 70)
print("REPOSITORY ANALYSIS")
print("=" * 70)

pprint(result)

print("=" * 70)