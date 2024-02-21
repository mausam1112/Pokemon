from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.source import ThirdParty
from app.config.settings import settings
from app.db import session, crud
from app.db.models import PokemonModel
from app.helpers import utils


router = APIRouter()

@router.get("/")
async def home():
    return JSONResponse(content="home", status_code=status.HTTP_200_OK)


@router.post("/add")
async def add_pokemon(
    data: PokemonModel,
    session: AsyncSession = Depends(session.get_session)
    ):
    try:
        await crud.insert_pokemons(
            data=data, 
            session=session
        )
        status_code=status.HTTP_201_CREATED
    except:
        status_code=status.HTTP_400_BAD_REQUEST
    return JSONResponse(content=None, status_code=status_code)


@router.get("/pokemons")
async def get_pokemons(session: AsyncSession = Depends(session.get_session)):
    if utils.read_tracker():
        '''Runs only one time'''
        third_party = ThirdParty()
        
        # read from third party api
        content = third_party.get_source_data()

        if isinstance(content, dict):
            for row in content.get('results'):
                try:
                    # extract required data
                    name = row['name']
                    url = row['url']
                    sub_contents = third_party.get_source_data(url)
                    img_str, types = third_party.parse_data(sub_contents)
                    
                    #
                    data = PokemonModel(name=name, image=img_str, type=types)

                    # store in db
                    await crud.insert_pokemons(
                        data=data, 
                        session=session
                    )
                except Exception as e:
                    print(f"Error: {e}")

            # update tracker to false
            utils.update_tracker()

    # finally return in either case
    try:
        result = await crud.get_pokemons(session=session)
        if result:
            status_code = status.HTTP_200_OK 
        else:
            status_code = status.HTTP_404_NOT_FOUND 
    except:
        result = None
        status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(content=result, status_code=status_code)


@router.get("/pokemon_by_name")
async def get_pokemon_by_name(
    name: str, 
    session: AsyncSession = Depends(session.get_session)
    ):
    
    try:
        result = await crud.get_by_name(session=session, name=name)
        if result:
            status_code = status.HTTP_200_OK 
        else:
            status_code = status.HTTP_404_NOT_FOUND 
    except:
        result = None
        status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(content=result, status_code=status_code)


