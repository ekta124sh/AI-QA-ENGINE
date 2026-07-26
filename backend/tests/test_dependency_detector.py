from backend.analyzers.dependency_detector import DependencyDetector

repo = "repositories/fastapi"

result = DependencyDetector.detect(repo)

print("=" * 60)

for key, value in result.items():
    print(f"{key:20}: {value}")

print("=" * 60)