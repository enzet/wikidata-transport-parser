"""Utility for network connections."""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

import urllib3

if TYPE_CHECKING:
    from pathlib import Path


def get(
    address: str, parameters: dict[str, str], cache_file: Path
) -> bytes | None:
    """Get data from the network."""

    if cache_file.exists():
        with cache_file.open("rb") as input_file:
            return input_file.read()

    pool: urllib3.PoolManager = urllib3.PoolManager()

    try:
        result = pool.request("GET", address, parameters)
    except urllib3.exceptions.MaxRetryError:
        return None

    time.sleep(1)

    pool.clear()
    if result.data:
        with cache_file.open("wb+") as output_file:
            output_file.write(result.data)
        return result.data

    return None
