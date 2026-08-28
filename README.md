# Mining Server API

A RESTful API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** for managing mining servers.
THIS SERVICE IS RUNNING PUBLICKLY IN THS URL https://mining-server-api-2.onrender.com/docs?utm_source=chatgpt.com

## Features

* Create mining servers
* View all mining servers
* View a specific server
* Update server information
* Delete mining servers
* Interactive Swagger API documentation

## Technologies

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic

## Installation

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint        | Description     |
| ------ | --------------- | --------------- |
| GET    | `/`             | API status      |
| POST   | `/servers`      | Create server   |
| GET    | `/servers`      | Get all servers |
| GET    | `/servers/{id}` | Get server      |
| PUT    | `/servers/{id}` | Update server   |
| DELETE | `/servers/{id}` | Delete server   |

## Project Structure

```text
main.py
database.py
models.py
schemas.py
crud.py
requirements.txt
```
