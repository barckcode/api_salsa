import datetime
from pydantic import BaseModel

class Singers_Model(BaseModel):
    id: str
    name: str
    country: str
    date_birth: datetime.date
    date_death: datetime.date
    description: str
