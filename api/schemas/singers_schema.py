import datetime
from typing import Optional
from pydantic import BaseModel


class SingersModel(BaseModel):
    id: str
    name: str
    country: str
    date_birth: datetime.date
    date_death: Optional[datetime.date]
    description: str
