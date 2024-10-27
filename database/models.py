from sqlalchemy import BigInteger, String, Column, ForeignKey
from sqlalchemy.orm import Declarative_base, Mapped, mapped_collumns
from sqlalchemy.ext.asyncio import AssyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(url="sqlite+aiosqlite:///database.sqlite3")

async_sessionmaker = async_sessionmaker(engine)

class Base(AssyncAttrs, Declarative_base):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_collumns(id, primary_key=True)
    tg_id = mapped_collumns(BigInteger)

class Profile(User):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_collumns(ForeignKey(User.id), primary_key=True)
    name: Mapped[str] = mapped_collumns(String(25), nullable=True)
    age: Mapped[int] = mapped_collumns(int, nullable=True)
    city: Mapped[str] = mapped_collumns(String(120), nullable=True)
    phone: Mapped[str] = mapped_collumns(String(40), nullable=True)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)