from sqlalchemy import Column, Integer, MetaData, String, Table

metadata_obj: MetaData = MetaData()

workers_table: Table = Table(
    "worker",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
