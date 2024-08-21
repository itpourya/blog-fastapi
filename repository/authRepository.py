from sqlalchemy.ext.asyncio import AsyncSession
from model.usersModel import User
from schema.inputs import RegisterInputs, UpdateUsernameInput, DeleteUserInput, GetUserInput
from schema.outputs import RegisterOutput
from sqlalchemy.ext.asyncio import AsyncSession
from exception.exceptions import UserNotFound
import sqlalchemy


class UserRepository:
    def __init__(self, data: RegisterInputs | UpdateUsernameInput | DeleteUserInput | GetUserInput,
                 db_session: AsyncSession) -> None:
        self.session = db_session
        self.data = data

    async def create_user(self) -> RegisterOutput:
        user = User(username=self.data.username, password=self.data.password, first_name=self.data.first_name,
                    last_name=self.data.last_name, active=True, email=self.data.email)

        async with self.session as session:
            session.add(user)
            await session.commit()

        return RegisterOutput(username=user.username, id=user.id)

    async def update_username(self) -> User:
        query = sqlalchemy.select(User).where(User.username == self.data.old_username)
        update_query = sqlalchemy.update(User).where(User.username == self.data.old_username).values(
            username=self.data.new_username)
        async with self.session as session:
            user_data = await session.scalar(query)

            if user_data is None:
                raise UserNotFound

            await session.execute(update_query)
            await session.commit()
            user_data.username = self.data.new_username
            return user_data

    async def delete_user(self) -> bool:
        query = sqlalchemy.delete(User).where(User.username == self.data.username, User.password == self.data.password)

        async with self.session as session:
            await session.execute(query)
            await session.commit()

        return True

    async def get_user(self) -> RegisterOutput:
        query = sqlalchemy.select(User).where(User.username == self.data.username)

        async with self.session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                raise UserNotFound

            return user_data
