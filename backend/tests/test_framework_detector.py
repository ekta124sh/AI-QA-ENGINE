from backend.analyzers.framework_detector import FrameworkDetector

repo = "repositories/fastapi"

framework = FrameworkDetector.detect(repo)

print("=" * 50)
print("Detected Framework:", framework)
print("=" * 50)