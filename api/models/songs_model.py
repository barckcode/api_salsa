from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Date, Integer, String
from config.db import meta, engine_postgres


songs_table = Table("songs", meta,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("name", String, nullable=False),
    Column("departure_date", Date, nullable=False),
)

meta.create_all(engine_postgres)
