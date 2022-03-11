import json
from pathlib import Path

from geomet import wkt
from sqlmodel import Session

from .database import create_tables, engine
from .models import Country

GEODATA_FILE_PATH = Path("data/natural-earth-admin0-v5-europe-3035.geojson").resolve()


def create_countries():
    with open(GEODATA_FILE_PATH) as file:
        country_features = json.load(file)["features"]

    country_instances = [
        Country(
            name=feature["properties"]["NAME"],
            population=int(feature["properties"]["POP_EST"]),
            geometry=wkt.dumps(feature["geometry"]),
        )
        for feature in country_features
    ]

    with Session(engine) as session:
        for instance in country_instances:
            session.add(instance)
            session.commit()


if __name__ == "__main__":
    create_tables()
    create_countries()
