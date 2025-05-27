"""Utility for network connections."""

import time
from pathlib import Path
from typing import Optional

import urllib3


def get(
    address: str, parameters: dict[str, str], cache_file: Path
) -> Optional[bytes]:
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
