FROM python:3.10.2-bullseye

ADD requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /srv/service
USER www-data
ADD . ./

CMD uvicorn geo_info_svg.api:app --host 0.0.0.0 --port 8000
