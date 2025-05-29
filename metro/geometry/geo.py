from __future__ import annotations

from dataclasses import dataclass

import numpy as np

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"


@dataclass
class Position:
    """Geographical position: longitude, latitude, and altitude."""

    longitude: float | None = None
    latitude: float | None = None
    altitude: float | None = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return False

        if (
            self.latitude is None
            or self.longitude is None
            or other.latitude is None
            or other.longitude is None
        ):
            return False
        return np.equal(self.longitude, other.longitude) and np.equal(
            self.latitude, other.latitude
        )

    @classmethod
    def from_structure(cls, structure: dict) -> Position:
        """Deserialize from structure."""
        longitude: float = structure["longitude"]
        latitude: float = structure["latitude"]
        altitude: float | None = structure.get("altitude")
        return cls(longitude, latitude, altitude)

    def to_structure(self) -> dict[str, float | None]:
        """Serialize to structure."""
        structure: dict[str, float | None] = {
            "longitude": self.longitude,
            "latitude": self.latitude,
        }
        if self.altitude is not None:
            structure["altitude"] = self.altitude
        return structure
