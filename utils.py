"""
Utility functions for environment variable management.

This module provides helper functions for safely retrieving and validating
environment variables required by the application.
"""

from os import getenv


def require_env(name: str) -> str:
    """
    Retrieve and validate a required environment variable.

    This function attempts to get an environment variable by name.
    If the variable is not set or is empty, it raises a RuntimeError.

    Args:
        name: The name of the environment variable to retrieve

    Returns:
        str: The value of the environment variable

    Raises:
        RuntimeError: If the environment variable is not set or is empty

    Example:
        >>> steam_path = require_env("steam_path")
        >>> # Returns the value if set, raises RuntimeError otherwise
    """
    value = getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is not set")
    return value
