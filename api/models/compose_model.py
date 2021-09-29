from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine_postgres


compositions_table = Table("compose", meta,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("id_singer", String, nullable=False),
    Column("id_song", Integer, nullable=False),
)

meta.create_all(engine_postgres)