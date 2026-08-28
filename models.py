from database import Base
from sqlalchemy import Column, Integer, String, Float


class Miningserver(Base):
    
 __tablename__="Mining_servers"

 id=Column(Integer,primary_key=True,index=True)
 name=Column(String,nullable=False)
 ip_address=Column(String,nullable=False)
 hashrate=Column(Float,nullable=False)
 temperature=Column(Float,nullable=False)
 status=Column(String,nullable=False)

