from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from geoalchemy2.types import Geometry
from sqlmodel import Session, cast, select

from .database import engine
from .models import Country

app = FastAPI()
templates = Jinja2Templates(directory="geo_info_svg/templates")


@app.get("/", response_class=HTMLResponse)
async def test(request: Request):
    with Session(engine) as session:
        countries = session.exec(
            select(
                Country.name,
                Country.population,
                cast(Country.geometry, Geometry).ST_XMin(),
                cast(Country.geometry, Geometry).ST_YMin(),
                cast(Country.geometry, Geometry).ST_XMax(),
                cast(Country.geometry, Geometry).ST_YMax(),
                Country.geometry.ST_AsSVG(),
            )
            .order_by(Country.population.desc())  # type: ignore
            .limit(10)
        ).all()

    return templates.TemplateResponse(
        "countries.html", {"request": request, "countries": countries}
    )
