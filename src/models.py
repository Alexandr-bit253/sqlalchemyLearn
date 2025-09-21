from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


# declarative-less
class Worker(Base):
    __tablename__ = "worker"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


metadata_obj: MetaData = MetaData()

# imperative-less
workers_table: Table = Table(
    "worker",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)

employer: Table = Table(
    "employer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
