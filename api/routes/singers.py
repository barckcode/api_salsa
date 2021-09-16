from fastapi import APIRouter, Response
from config.db import db_connection
from models.singers_model import singers_table
from schemas.singers_schema import Singers_Model


# Init Route
singers = APIRouter()


# Routes
#@singers.get("/singers", response_model=list[Singers_Model], tags=["Cantantes"])
@singers.get("/singers", tags=["Cantantes"])
def get_all_singers():
    return db_connection.execute(singers_table.select()).fetchall()
