
import asyncio

from models import Students, Roles
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

async def add_role(name, level):
    PG_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

    engine =  create_async_engine(PG_URL)

    session = sessionmaker(
        engine,
        class_ = AsyncSession,
        expire_on_commit=False
    )

    role = Roles(name=name, level=level)

    async with session() as db:
        db.add(role)
        await db.commit()

        return role


class RoleService():

    def __init__(self, db_url):
        self.db_url = db_url


    def get_async_session(self) -> AsyncSession:

        engine =  create_async_engine(self.db_url)


        return sessionmaker(
            engine,
            class_ = AsyncSession,
            expire_on_commit=False
        )


    async def add_role(self, name, level):

        session = self.get_async_session()

        role = Roles(name=name, level=level)

        async with session() as db:
            db.add(role)
            await db.commit()

            return role



    async def get_roles(self):

        session = self.get_async_session()

        async with session() as db:

            roles = await db.execute(select(Roles))
            return roles.scalars().all()


    async def get_role(self, id):

        session = self.get_async_session()

        async with session() as db:

            roles = await db.execute(select(Roles).where(Roles.id==id))
            return roles.one()


class StudentsService():

    def __init__(self, db_url):
        self.db_url = db_url

    def get_async_session(self) -> AsyncSession:

        engine =  create_async_engine(self.db_url)


        return sessionmaker(
            engine,
            class_ = AsyncSession,
            expire_on_commit=False
        )


    async def get_Students(self, id):
        session = self.get_async_session()

        async with session() as db:

            Students = await db.execute(select(Students).where(Students.id==id))
            return Students.one()


    async def add_Students(self, login, password, role):

        session = self.get_async_session()

        Students = Students(login=login, password=password, role=role)

        async with session() as db:
            db.add(Students)
            await db.commit()

            return Students
        

    async def update_Students(self, id, **kwargs):
        
        session = self.get_async_session()

        async with session() as db:
            Students = await db.execute(select(Students).where(Students.id==id))

            Students = Students.scalars().one()
            

            print(Students)

            for key, value in kwargs.items():
                setattr(Students, key, value)

            await db.commit()

            return Students
        
    
    async def del_Students(self, id):
        session = self.get_async_session()

        async with session() as db:
            Students = await db.execute(delete(Students).where(Students.id==id))

            await db.commit()

            return Students



async def runner():
    PG_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

    role_service = RoleService(PG_URL)

    Students_service = StudentsService(PG_URL)

    res = await Students_service.del_Students(1)

    print(res)


if __name__ == "__main__":

    asyncio.run(runner())
    