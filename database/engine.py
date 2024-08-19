from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

SQL_ALCHEMY_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(
    url=SQL_ALCHEMY_URL,
)

SessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
