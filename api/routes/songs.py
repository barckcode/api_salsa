from os import name
from fastapi import APIRouter
from sqlalchemy.sql.elements import between
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

# Internal Modules
from config.db import db_connection
from models.singers_model import singers_table
from models.compose_model import compositions_table
from models.songs_model import songs_table
from schemas.songs_schema import SongsModel
from schemas.songs_schema_db import SongsModelDb


# Init Route
songs_routes = APIRouter()


# Routes
@songs_routes.get("/singers/{id_singer}/songs", tags=["Canciones"])
async def get_all_songs_by_singer(id_singer: str):
    compositions = db_connection.execute(compositions_table.select().where(compositions_table.c.id_singer == id_singer)).fetchall()

    list_songs = []
    for data in compositions:
        _, _, id_song = data
        song = db_connection.execute(songs_table.select().where(songs_table.c.id == id_song)).first()
        list_songs.append(song)

    singer = db_connection.execute(singers_table.select().where(singers_table.c.id == id_singer)).first()

    return {
        "singer": singer.name,
        "songs": list_songs
    }


@songs_routes.get("/singers/{id_singer}/songs/{id_song}", response_model=SongsModel, tags=["Canciones"])
async def get_song_by_id(id_singer: str, id_song: int):
    singer = db_connection.execute(singers_table.select().where(singers_table.c.id == id_singer)).first()
    song = db_connection.execute(songs_table.select().where(songs_table.c.id == id_song)).first()

    composition_validation = db_connection.execute(
        compositions_table.select().where(compositions_table.c.id_singer == id_singer, compositions_table.c.id_song == id_song)
    ).first()

    if composition_validation:
        return {
            "id": song.id,
            "name": song.name,
            "departure_date": song.departure_date,
            "singer": singer.name
        }
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


@songs_routes.post("/singers/{id_singer}/songs", response_model=SongsModel, tags=["Canciones"])
async def added_new_song(id_singer: str, song: SongsModelDb):
    singer_validation = db_connection.execute(singers_table.select().where(singers_table.c.id == id_singer)).first()

    if singer_validation:
        new_song = {
            "name": song.name,
            "departure_date": song.departure_date
        }

        db_connection.execute(songs_table.insert().values(new_song))
        last_song_insert = db_connection.execute(songs_table.select().where(songs_table.c.name == song.name)).first()

        new_composition = {
            "id_singer": id_singer,
            "id_song": last_song_insert.id
        }

        db_connection.execute(compositions_table.insert().values(new_composition))
        singer = db_connection.execute(singers_table.select().where(singers_table.c.id == id_singer)).first()
        return {
            "id": last_song_insert.id,
            "name": last_song_insert.name,
            "departure_date": last_song_insert.departure_date,
            "singer": singer.name
        }
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


@songs_routes.delete("/singers/{id_singer}/songs/{id_song}", status_code=HTTP_204_NO_CONTENT, tags=["Canciones"])
async def delete_song(id_singer: str, id_song: int):
    composition_validation = db_connection.execute(
        compositions_table.select().where(compositions_table.c.id_singer == id_singer, compositions_table.c.id_song == id_song)
    ).first()

    if composition_validation:
        db_connection.execute(songs_table.delete().where(songs_table.c.id == id_song))
        db_connection.execute(songs_table.delete().where(compositions_table.c.id_song == id_song))
        return Response(status_code=HTTP_204_NO_CONTENT)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


@songs_routes.put("/singers/{id_singer}/songs/{id_song}", response_model=SongsModel, tags=["Canciones"])
async def update_song(id_singer: str, id_song: int, song: SongsModelDb):
    composition_validation = db_connection.execute(
        compositions_table.select().where(compositions_table.c.id_singer == id_singer, compositions_table.c.id_song == id_song)
    ).first()

    if composition_validation:
        db_connection.execute(songs_table.update().values(
            name = song.name,
            departure_date = song.departure_date
        ).where(songs_table.c.id == id_song))

        last_song_insert = db_connection.execute(songs_table.select().where(songs_table.c.id == id_song)).first()
        singer = db_connection.execute(singers_table.select().where(singers_table.c.id == id_singer)).first()

        return {
            "id": last_song_insert.id,
            "name": last_song_insert.name,
            "departure_date": last_song_insert.departure_date,
            "singer": singer.name
        }
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

