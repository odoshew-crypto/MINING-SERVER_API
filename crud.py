from sqlalchemy.orm import Session
import schemas
import models

def create_server(db:Session, data: schemas.MiningserverCreate):
    db_server = models.Miningserver(**data.model_dump())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)

    return db_server

def get_servers(db:Session):
    return db.query(models.Miningserver).all()

def get_server(db:Session,server_id:int):
    return db.query(models.Miningserver).filter(models.Miningserver.id==server_id).first()

def update_server(db:Session,server_id:int,data:schemas.MiningserverUpdate):
    server= db.query(models.Miningserver).filter(models.Miningserver.id==server_id).first()
  
    if server is None:
        return None
    
    update=data.model_dump(exclude_unset=True)
    for key, value in update.items():
        setattr(server, key, value)

    db.commit()
    db.refresh(server) 

    return server 

def delete_server(db:Session,server_id:id):
    server=db.query(models.Miningserver).filter(models.Miningserver.id==server_id).first()

    if server  is None:
        return None
    db.delete(server)
    db.commit()
    return server
    


