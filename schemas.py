from pydantic import BaseModel

class MiningserverCreate(BaseModel):
   
    name:str
    ip_address:str
    hashrate:float
    temperature:float
    status:str


class MiningserverUpdate(BaseModel):
    name:str
    ip_address:str
    hashrate:float
    temperature:float
    status:str

class MiningserverResponse(BaseModel):
    id:int
    name:str
    ip_address:str
    hashrate:float
    temperature:float
    status:str
class config: 
    Attribute=True  
        