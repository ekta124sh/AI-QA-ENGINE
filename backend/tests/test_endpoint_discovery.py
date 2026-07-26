from backend.analyzers.endpoint_discovery import EndpointDiscovery
from backend.services.git_service import GitService


def main():
    print("=" * 80)
    print("Cloning Repository...")
    print("=" * 80)

    repo = GitService.clone_repository(
        "https://github.com/fastapi/fastapi"
    )

    print(f"Repository: {repo}")

    print("=" * 80)
    print("Discovering Endpoints...")
    print("=" * 80)

    endpoints = EndpointDiscovery.discover(repo)

    print(f"\nTotal Endpoints Found: {len(endpoints)}\n")

    for endpoint in endpoints[:20]:
        print(endpoint)


if __name__ == "__main__":
    main()