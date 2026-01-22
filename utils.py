from os import getenv


def require_env(name: str) -> str:
    value = getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is not set")
    return value
