from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:Odoshe2003@localhost:5432/mining_db"
engine=create_engine(DATABASE_URL)

sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine

)

Base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close    

        
