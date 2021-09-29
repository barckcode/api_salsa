from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Date, String
from config.db import meta, engine_postgres

singers_table = Table("singers", meta,
    Column("id", String, primary_key=True, unique=True, nullable=False),
    Column("name", String, nullable=False),
    Column("country", String, nullable=False),
    Column("date_birth", Date, nullable=False),
    Column("date_death", Date, nullable=True),
    Column("description", String, nullable=False)
)

meta.create_all(engine_postgres)
