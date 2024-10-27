
from sqlalchemy import BigInteger, String, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

create_engine = create_async_engine(url='sqlite+aiosqlite:///database.sqlite3')

async_sessionmaker = async_sessionmaker(create_engine, echo=True)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger)

# class Profile(Base):
#     __tablename__ = 'profiles'

#     id: Mapped[int] = mapped_column(int, primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     name: Mapped[str] = mapped_column(String(25))
#     age: Mapped[int] = mapped_column(int)
#     city: Mapped[str] = mapped_column(String(120))
#     phone: Mapped[str] = mapped_column(String(40))

async def async_main():
    async with create_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)