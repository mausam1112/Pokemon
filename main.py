import uvicorn

from fastapi import FastAPI
from app.api.v1 import pokemon
from app.db import session

async def init_models():
    async with session.engine.begin() as conn:
        # await conn.run_sync(session.Base.metadata.drop_all)
        await conn.run_sync(session.Base.metadata.create_all)

_ = init_models()

app = FastAPI()

app.include_router(pokemon.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000)
