"""Test Wikidata parser."""

from __future__ import annotations

from pathlib import Path

from metro.core.system import Map, System
from metro.harvest.wikidata import WikidataCityParser, WikidataParser


class MockWikidataParser(WikidataParser):
    """Mock Wikidata parser."""

    @staticmethod
    def parse_wikidata(wikidata_id: int) -> dict | None:
        """Parse Wikidata item."""

        if wikidata_id in [1, 2]:
            return {"entities": {f"Q{wikidata_id}": {"claims": {}}}}
        return None


def test_simple() -> None:
    """Test simple case with mock parser."""

    wikidata_parser: MockWikidataParser = MockWikidataParser(
        cache_directory=Path("cache")
    )
    map_: Map = Map("test_map")
    map_.local_languages = ["cz"]
    map_.systems = {"metro": System({}, "metro")}
    parser: WikidataCityParser = WikidataCityParser(
        wikidata_parser=wikidata_parser,
        map_=map_,
        systems_dict={1: "metro"},
        wikidata_init_ids=[2],
        wikidata_id=1,
        network_update=[],
    )
    parser.parse()
