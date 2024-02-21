from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db.models import PokemonModel


async def insert_pokemons(
        data: PokemonModel,
        session: AsyncSession
    ):
    '''
    Adds data into table
    '''

    session.add(data)
    await session.commit()
    await session.refresh(data)

async def get_pokemons(session: AsyncSession):
    '''
    Retrieve data from table
    '''
    query = select(PokemonModel)
    response = await session.execute(query)

    result = []
    for row in response.fetchall():
        row = row[0]
        result.append(
            {
                'name':row.name, 
                'image':row.image, 
                'type':row.type#.split(',')
            }
        )
    return result

async def get_by_name(session: AsyncSession, name: str):
    '''
    Retrieve data from table by name field.
    '''
    query = select(PokemonModel).where(PokemonModel.name==name)
    response = await session.execute(query)

    result = []
    for row in response.fetchall():
        row = row[0]
        result.append(
            {
                'name':row.name, 
                'image':row.image, 
                'type':row.type#.split(',')
            }
        )
    return result
