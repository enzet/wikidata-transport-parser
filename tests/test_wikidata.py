"""Test Wikidata parser."""

from metro.core.system import Map, System
from metro.harvest.wikidata import WikidataCityParser


class MockWikidataParser:
    """Mock Wikidata parser."""

    @staticmethod
    def parse_wikidata(wikidata_id: int) -> dict:
        """Parse Wikidata item."""

        if wikidata_id in [1, 2]:
            return {"entities": {f"Q{wikidata_id}": {"claims": {}}}}
        return None


def test_simple() -> None:
    """Test simple case with mock parser."""

    wikidata_parser: MockWikidataParser = MockWikidataParser()
    map_: Map = Map("test_map")
    map_.local_languages = ["cz"]
    map_.systems = {"metro": System({}, "metro")}
    parser: WikidataCityParser = WikidataCityParser(
        wikidata_parser, map_, {1: "metro"}, [2], 1, []
    )
    parser.parse()
