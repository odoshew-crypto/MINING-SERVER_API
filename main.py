from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, get_db


models.Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Mining Server API",
    description="API for managing mining servers",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Mining Server API is running"
    }


@app.post(
    "/servers",
    response_model=schemas.MiningserverResponse
)
def create_server(
    data: schemas.MiningserverCreate,
    db: Session = Depends(get_db)
):

    return crud.create_server(
        db,
        data
    )


@app.get(
    "/servers",
    response_model=list[schemas.MiningserverResponse]
)
def get_servers(
    db: Session = Depends(get_db)
):

    return crud.get_servers(db)


@app.get(
    "/servers/{server_id}",
    response_model=schemas.MiningserverResponse
)
def get_server(
    server_id: int,
    db: Session = Depends(get_db)
):

    server = crud.get_server(
        db,
        server_id
    )

    if server is None:

        raise HTTPException(
            status_code=404,
            detail="Mining server not found"
        )

    return server


@app.put(
    "/servers/{server_id}",
    response_model=schemas.MiningserverResponse
)
def update_server(
    server_id: int,
    data: schemas.MiningserverUpdate,
    db: Session = Depends(get_db)
):

    server = crud.update_server(
        db,
        server_id,
        data
    )

    if server is None:

        raise HTTPException(
            status_code=404,
            detail="Mining server not found"
        )

    return server


@app.delete(
    "/servers/{server_id}"
)
def delete_server(
    server_id: int,
    db: Session = Depends(get_db)
):

    server = crud.delete_server(
        db,
        server_id
    )

    if server is None:

        raise HTTPException(
            status_code=404,
            detail="Mining server not found"
        )

    return {
        "message": "Mining server deleted successfully",
        "server_id": server_id
    }

