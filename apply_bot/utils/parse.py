from typing import Any

from toml import dumps


def to_toml(data: dict[str, Any]) -> str:
    return dumps(data)
