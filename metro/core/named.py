"""Named objects."""

from __future__ import annotations

import logging
from dataclasses import dataclass

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"


@dataclass
class Named:
    """Something that has proper names in different languages."""

    names: dict[str, str]
    """Proper names in different languages."""

    def set_name(
        self, language: str, name: str, *, ignore_rewrite: bool = True
    ) -> None:
        """Set name in specified language."""
        if (
            language in self.names
            and not ignore_rewrite
            and self.names[language] != name
        ):
            logging.warning(
                "rewrite name: %s -> %s", self.names[language], name
            )
        self.names[language] = name

    def set_names(
        self, names: dict[str, str], *, ignore_rewrite: bool = True
    ) -> None:
        """Set names of the object."""

        [
            self.set_name(
                language, names[language], ignore_rewrite=ignore_rewrite
            )
            for language in names
        ]

    def has_name(self, language: str) -> bool:
        """Check if object has name in specified language."""

        return language in self.names or "int" in self.names

    def get_name(self, language: str) -> str | None:
        """Get name in specified language."""

        if language in self.names:
            return self.names[language]
        if "int" in self.names:
            return self.names["int"]
        return None
