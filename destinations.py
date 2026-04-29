"""Inverness Airport (INV) destinations — April 2026."""

DESTINATIONS = {
    "INV": {
        "name": "Inverness",
        "routes": {
            "AMS": "Amsterdam",
            "BHD": "Belfast City",
            "BHX": "Birmingham",
            "BRS": "Bristol",
            "DUB": "Dublin",
            "KOI": "Kirkwall",
            "LGW": "London Gatwick",
            "LHR": "London Heathrow",
            "LPA": "Gran Canaria",
            "LSI": "Sumburgh",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "PMI": "Palma",
            "RVN": "Rovaniemi",
            "SYY": "Stornoway",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
