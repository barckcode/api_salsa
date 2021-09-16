from pydantic import BaseModel

class Singers_Model(BaseModel):
    id: str
    name: str
    country: str
    date_birth: str
    date_death: str
    description: str
