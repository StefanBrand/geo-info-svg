from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from .database import engine
from .models import Country

app = FastAPI()
templates = Jinja2Templates(directory="geo_info_svg/templates")


@app.get("/", response_class=HTMLResponse)
async def test(request: Request):
    with Session(engine) as session:
        countries = session.exec(select(Country)).all()
        return templates.TemplateResponse(
            "countries.html", {"request": request, "countries": countries}
        )
