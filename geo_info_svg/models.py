from typing import Optional

from geoalchemy2.types import Geometry
from sqlmodel import Column, Field, SQLModel


class Country(SQLModel, table=True):
    class Config:
        arbitrary_types_allowed = True

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    population: int
    geometry: Geometry = Field(
        sa_column=Column(Geometry(geometry_type="POLYGON", srid=3035))
    )
