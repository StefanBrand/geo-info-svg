from typing import Optional

from geoalchemy2.types import Geometry
from sqlmodel import Field, SQLModel


class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    population: int
    geometry: str = Field(sa_column=Geometry(geometry_type="POLYGON", srid=3035))
