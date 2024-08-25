from repository.authRepository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from schema.inputs import RegisterInputs, UpdateUsernameInput, GetUserInput, DeleteUserInput
from schema.outputs import RegisterOutput, GetUserOutput
from model.usersModel import User
import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


@pytest.fixture
def session():
    SQL_ALCHEMY_URL = "sqlite+aiosqlite:///./blog.db"
    engine = create_async_engine(
        url=SQL_ALCHEMY_URL,
    )
    SessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

    db = SessionLocal()
    return db


@pytest.fixture
def register_data():
    return RegisterInputs(
        username="testuser",
        password="password",
        first_name="Test",
        last_name="User",
        email="test@example.com"
    )


@pytest.fixture
def update_data():
    return UpdateUsernameInput(
        old_username="testuser",
        new_username="newtestuser"
    )


@pytest.fixture
def getuser_data():
    return GetUserInput(
        username="newtestuser",
    )


@pytest.fixture
def delete_data():
    return DeleteUserInput(
        username="newtestuser",
        password="password"
    )


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession, register_data):
    repository = UserRepository(data=register_data, db_session=session)

    result = await repository.create_user()

    assert isinstance(result, RegisterOutput)
    assert result.username == register_data.username


@pytest.mark.asyncio
async def test_update_username(session: AsyncSession, update_data):
    repository = UserRepository(data=update_data, db_session=session)

    result = await repository.update_username()

    assert isinstance(result, User)
    assert result.username == update_data.new_username


@pytest.mark.asyncio
async def test_get_user_by_username(session: AsyncSession, getuser_data):
    repository = UserRepository(data=getuser_data, db_session=session)

    result = await repository.get_user()

    assert isinstance(result, User)
    assert result.username == getuser_data.username


@pytest.mark.asyncio
async def test_delete_user(session: AsyncSession, delete_data):
    repository = UserRepository(data=delete_data, db_session=session)

    result = await repository.delete_user()

    assert result == True
