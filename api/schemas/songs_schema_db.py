import datetime
from typing import Optional
from pydantic import BaseModel


class SongsModelDb(BaseModel):
    id: Optional[int]
    name: str
    departure_date: datetime.date
