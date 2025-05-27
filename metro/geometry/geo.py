from typing import Optional

import numpy as np

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"


class Position:
    """Geographical position: longitude, latitude, and altitude."""

    def __init__(
        self,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        altitude: Optional[float] = None,
    ):
        self.longitude: Optional[float] = longitude
        self.latitude: Optional[float] = latitude
        self.altitude: Optional[float] = altitude

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
    def from_structure(cls, structure: dict) -> "Position":
        """Deserialize from structure."""
        longitude: float = structure["longitude"]
        latitude: float = structure["latitude"]
        altitude: Optional[float] = structure.get("altitude")
        return cls(longitude, latitude, altitude)

    def to_structure(self) -> dict[str, Optional[float]]:
        """Serialize to structure."""
        structure = {"longitude": self.longitude, "latitude": self.latitude}
        if self.altitude is not None:
            structure["altitude"] = self.altitude
        return structure
