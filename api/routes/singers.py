from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

# Internal Modules
from config.db import db_connection
from models.singers_model import singers_table
from schemas.singers_schema import SingersModel


# Init Route
singers_routes = APIRouter()


# Routes
#@singers.get("/singers", response_model=list[SingersModel], tags=["Cantantes"])
@singers_routes.get("/singers", tags=["Cantantes"])
async def get_all_singers():
    return db_connection.execute(singers_table.select()).fetchall()


@singers_routes.get("/singers/{id}", response_model=SingersModel, tags=["Cantantes"])
async def get_singer_by_id(id: str):
    return db_connection.execute(singers_table.select().where(singers_table.c.id == id)).first()


@singers_routes.post("/singers", response_model=SingersModel, tags=["Cantantes"])
async def create_new_singer(singer: SingersModel):
    new_singer = {
        "id": singer.id,
        "name": singer.name,
        "country": singer.country,
        "date_birth": singer.date_birth,
        "date_death": singer.date_death,
        "description": singer.description
    }

    db_connection.execute(singers_table.insert().values(new_singer))
    return db_connection.execute(singers_table.select().where(singers_table.c.id == singer.id)).first()


@singers_routes.delete("/singers/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Cantantes"])
async def delete_singer_by_id(id: str):
    db_connection.execute(singers_table.delete().where(singers_table.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@singers_routes.put("/singers/{id}", response_model=SingersModel, tags=["Cantantes"])
async def update_singer_by_id(id: str, singer: SingersModel):
    db_connection.execute(singers_table.update().values(
        id = singer.id,
        name = singer.name,
        country = singer.country,
        date_birth = singer.date_birth,
        date_death = singer.date_death,
        description = singer.description
    ).where(singers_table.c.id == id))

    return db_connection.execute(singers_table.select().where(singers_table.c.id == id)).first()
