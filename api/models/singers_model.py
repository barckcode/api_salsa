from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, DATETIME
from config.db import meta, engine_postgres

singers_table = Table("singers", meta,
    Column("id", String, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("name", String, nullable=False),
    Column("country", String, nullable=False),
    Column("date_birth", String, nullable=False),
    Column("date_death", String, nullable=True),
    Column("description", String, nullable=False)
)

meta.create_all(engine_postgres)
