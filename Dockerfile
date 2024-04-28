FROM python:3.11 AS pybird_builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgeoip-dev python3-pyproj python3-psycopg2 python3-gdal python3-poetry && apt-get clean all

RUN python -mvenv /env && . /env/bin/activate && pip install poetry && pip install gunicorn

COPY . /app

WORKDIR /app

RUN . /env/bin/activate && poetry install --no-root

FROM pybird_builder AS pybird_tester

ENTRYPOINT [ "/env/bin/poetry", "run", "./manage.py", "test" ]

FROM pybird_builder AS pybird

EXPOSE 8000

ENTRYPOINT [ "/env/bin/gunicorn", "--bind", ":8000", "pybird.wsgi" ]
