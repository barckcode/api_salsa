import datetime
from typing import Optional
from pydantic import BaseModel


class SongsModel(BaseModel):
    id: Optional[int]
    name: str
    departure_date: datetime.date
    singer: str
