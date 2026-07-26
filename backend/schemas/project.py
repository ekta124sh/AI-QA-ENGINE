from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str
    github_url: str


class ProjectResponse(ProjectCreate):
    id: int
    status: str

    class Config:
        from_attributes = True