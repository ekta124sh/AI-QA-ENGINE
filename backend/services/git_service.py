import os
from git import Repo


class GitService:

    CLONE_DIRECTORY = "repositories"

    @classmethod
    def clone_repository(cls, github_url: str):

        os.makedirs(cls.CLONE_DIRECTORY, exist_ok=True)

        repo_name = github_url.split("/")[-1].replace(".git", "")

        repo_path = os.path.join(cls.CLONE_DIRECTORY, repo_name)

        if os.path.exists(repo_path):
            return repo_path

        Repo.clone_from(github_url, repo_path)

        return repo_path