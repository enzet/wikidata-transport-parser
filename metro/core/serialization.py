"""Serialization of primitive values."""

from datetime import datetime
from enum import Enum
from typing import Any

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"


def is_null(value: Any) -> bool:
    """Check if value is null or empty, but not zero."""

    return value is None or value == {} or value == []


def serialize(value: Any) -> Any:
    """Serialize primitive value."""
    for type_ in str, int, float:
        if isinstance(value, type_):
            return value
    if isinstance(value, list):
        return [serialize(x) for x in value]
    if isinstance(value, tuple):
        return [serialize(x) for x in value]
    if isinstance(value, dict):
        return {x: serialize(y) for x, y in value.items()}
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    return value.serialize()


def deserialize(value: Any) -> Any:
    """Deserialize primitive value."""
    for type_ in str, int, float:
        if isinstance(value, type_):
            return value
    if isinstance(value, list):
        return [deserialize(x) for x in value]
    if isinstance(value, dict):
        return {x: deserialize(y) for x, y in value.items()}
    return value.deserialize()
