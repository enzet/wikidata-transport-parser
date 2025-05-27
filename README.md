# Transport Network Parser for Wikidata

A [Wikidata](https://wikidata.org) parser for transport networks.

## Installation

Requirements: Python 3.9 or higher.

```shell
pip install .
```

## Wikidata Parsing

The algorithm takes as input a Wikidata identifier of an arbitrary transport
station and a Wikidata identifier of the transport system. The algorithm will
recursively parse the network structure.

## Example Run

To parse the Prague metro system, you need to specify the system's Wikidata item
([Q190271](https://www.wikidata.org/wiki/Q190271) for Prague Metro) and
any station's Wikidata item
([Q1877386](https://www.wikidata.org/wiki/Q1877386) for Florenc metro station).

```shell
metro --system 190271 --station 1877386
```

## Output

The result will be saved in the `out/metro.json` file with the following structure:

```json
{
    "id": "<TEXT IDENTIFIER>",
    "stations": ["<STATION STRUCTURE>"],
    "lines": ["<LINE STRUCTURE>"]
}
```

### Station Structure

```json
{
    "id": "<LINE IDENTIFIER>/<STATION SHORT IDENTIFIER>",
    "line": "<LINE IDENTIFIER>",
    "names": {
        "<LANGUAGE>": "<NAME>"
    },
    "open_time": "",
    "geo_positions": ["<LATITUDE>", "<LONGITUDE>"],
    "connections": [
        {
            "to": "<OTHER STATION IDENTIFIER>",
            "type": "<CONNECTION TYPE>"
        }
    ],
    "site_links": [
        {
            "<SITE>": "<PAGE NAME>"
        }
    ]
}
```

### Line Structure

```json
{
    "id": "<LINE IDENTIFIER>/<STATION SHORT IDENTIFIER>",
    "names": {
        "<LANGUAGE>": "<NAME>"
    },
    "color": "<LINE COLOR>"
}
```
