from sqlalchemy import Column, Integer, Text, VARCHAR
from sqlmodel import Field, SQLModel

from app.config.settings import settings
from app.db.session import Base


class PokemonBase(SQLModel):
    id: int = Field(
        primary_key=True,
        index=True,
        nullable=False
    )
    name: str = Field()
    image: str = Field()
    type: str = Field()


class PokemonCreate(PokemonBase):
    ...


class PokemonModel(PokemonBase, table=True):
    __tablename__ = settings.table_name
