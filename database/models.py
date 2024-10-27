
from sqlalchemy import BigInteger, String, Column, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

create_engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_sessionmaker = async_sessionmaker(create_engine, echo=True)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger)

class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = Column(BigInteger, primary_key=True)
    user_id: Mapped[int] = Column(ForeignKey('users.id'))
    name: Mapped[str] = Column(String(25))
    age: Mapped[int] = Column(Integer)
    city: Mapped[str] = Column(String(120))
    phone: Mapped[str] = Column(String(40))

async def async_main():
    async with create_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)