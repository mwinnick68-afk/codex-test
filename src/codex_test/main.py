from __future__ import annotations

import argparse
import sys
import unicodedata
from collections.abc import Sequence

_MAX_NAME_LENGTH = 128


def _normalize_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    normalized_name = unicodedata.normalize("NFKC", name).strip()
    if not normalized_name:
        raise ValueError("name must not be empty")
    if len(normalized_name) > _MAX_NAME_LENGTH:
        raise ValueError(f"name must be {_MAX_NAME_LENGTH} characters or fewer")

    # Block terminal/control characters to avoid log/terminal output abuse.
    if any(unicodedata.category(char).startswith("C") for char in normalized_name):
        raise ValueError("name contains unsupported control characters")
    return normalized_name


def greet(name: str) -> str:
    """Return a safe greeting for the provided name."""
    safe_name = _normalize_name(name)
    return f"Hello, {safe_name}!"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print a greeting")
    parser.add_argument("name", nargs="?", default="world", help="Name to greet")
    args = parser.parse_args(argv)

    try:
        print(greet(args.name))
    except (TypeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
