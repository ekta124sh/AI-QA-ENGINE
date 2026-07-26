from backend.services.pipeline_service import PipelineService


PipelineService.generate_testcases(
    repo_url="https://github.com/fastapi/fastapi.git",
    project_id=1
)