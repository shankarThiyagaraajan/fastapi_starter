# FastAPI - Starter Setup
[![Packagist](https://img.shields.io/badge/FastAPI-0.115.6-blue?logo=fastapi&logoColor=green)](https://github.com/shankarThiyagaraajan/fastapi_starter) [![Packagist](https://img.shields.io/badge/Python-3.12.x-blue?logo=python&logoColor=white)](https://github.com/shankarThiyagaraajan/fastapi_starter) [![Packagist](https://img.shields.io/badge/Docker-Ready-greeb?logo=docker&logoColor=white)](https://github.com/shankarThiyagaraajan/fastapi_starter) [![Packagist](https://img.shields.io/badge/SQLAlchemy-2.0.36-red?logo=SQLAlchemy&logoColor=white)](https://github.com/shankarThiyagaraajan/fastapi_starter) [![Packagist](https://img.shields.io/badge/Test-Success-greeb?logo=SQLAlchemy&logoColor=white)](https://github.com/shankarThiyagaraajan/fastapi_starter)

# Packages Included
Essential packages for  FastAPI-Boilerplate as following,

|                |Package Version                          |Purpose                         |
|----------------|-------------------------------|-----------------------------|
|Python |3.12.x            |Backend            |
|FastAPI          |0.115.6            |Framework - ASGI           |
|PostgreSQL          |16.3|Database|
|SQLAlchemy          |2.0.36|ORM for Database|
|APScheduler          |3.11.0|Cron and Background Tasks|
|logzero          |1.7.0|Logger|


# Installation

## Base App
``` base
$ git clone https://github.com/shankarThiyagaraajan/fastapi_starter.git <your-project-name>
```
```bash
$ cd <your-project-name>
$ python3 -m venv env    # Optional setup for Virtual Environment
$ pip install -r requirements.txt
```

## Database via Docker
```bash
$ docker compose up -d
```

## For DB Migrations:
```bash
$ alembic revision --autogenerate -m "Your Quick Migration Note"
$ alembic upgrade head
```

## To Start App
```bash
$ fastapi dev main.py
```

> **Debug:** Default setup is ready to support VsCode debugger

## To Test App
```bash
$ pytest
```

Happy Coding...!