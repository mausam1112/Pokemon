from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import(
    AsyncSession, create_async_engine, async_sessionmaker
)
from app.config.settings import settings


def create_database_url():
    '''
    Format the connection string of database.
    '''
    # "postgresql+asyncpg://postgres:root@localhost/pokemon_info"
    prefix = "postgresql+asyncpg://"
    database_url = f"{prefix}{settings.db_user}:{settings.db_pw}@{settings.db_host}/{settings.db_name}"
    return database_url

engine = create_async_engine(
    # settings.database_url,
    create_database_url(),
    future=True,
    pool_size=max(5, int(settings.postgres_pool_size)),
)

SessionLocal = async_sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()

async def get_session():
    '''
    Initiate Session for database operation.
    '''
    async with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
