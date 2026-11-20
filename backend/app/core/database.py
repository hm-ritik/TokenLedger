from app.core.config import setting
from sqlalchemy.ext.asyncio import AsyncSession , create_async_engine , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Database:
    def __init__(self,url:str):
        self.engine=create_async_engine(url , pool_pre_ping=True)
        self._sessionmaker=async_sessionmaker(bind=self.engine ,  expire_on_commit=False,autoflush=False)

    async def get_session(self):
        async with self._sessionmaker() as session:
            yield session

    async def get_dispose(self):
         await self.engine.dispose()         
            
db=Database(setting.DATABASE_URL)

        