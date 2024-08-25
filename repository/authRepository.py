from sqlalchemy.ext.asyncio import AsyncSession
from model.usersModel import User
from schema.inputs import RegisterInputs, UpdateUsernameInput, DeleteUserInput, LoginInput, GetUserInput
from schema.outputs import RegisterOutput, GetUserOutput
from sqlalchemy.ext.asyncio import AsyncSession
from exception.exceptions import UserNotFound
import sqlalchemy
from logger.log import getLogger


class UserRepository:
    def __init__(self, data: RegisterInputs | UpdateUsernameInput | DeleteUserInput | LoginInput | GetUserInput,
                 db_session: AsyncSession) -> None:
        self.session = db_session
        self.data = data
        self.logger = getLogger("info")

    async def create_user(self) -> RegisterOutput:
        user = User(username=self.data.username, password=self.data.password, first_name=self.data.first_name,
                    last_name=self.data.last_name, active=True, email=self.data.email)

        async with self.session as session:
            session.add(user)
            await session.commit()

        self.logger.info(f"User {user.id} - {user.username} - created")

        return RegisterOutput(username=user.username, id=user.id)

    async def update_username(self) -> User:
        query = sqlalchemy.select(User).where(User.username == self.data.old_username)
        update_query = sqlalchemy.update(User).where(User.username == self.data.old_username).values(
            username=self.data.new_username)

        async with self.session as session:
            user_data = await session.scalar(query)

            if user_data is None:
                self.logger.info(f"User - {self.data.username} - NOT FOUND DB")
                raise UserNotFound

            await session.execute(update_query)
            await session.commit()
            user_data.username = self.data.new_username

            self.logger.info(f"User {user_data.id} - {user_data.username} - Updated")

            return user_data

    async def delete_user(self) -> bool:
        query = sqlalchemy.delete(User).where(User.username == self.data.username, User.password == self.data.password)
        query_findUser = sqlalchemy.select(User).where(User.username == self.data.username)

        async with self.session as session:
            user_data = await session.scalar(query_findUser)
            if user_data is None:
                self.logger.info(f"User {self.data.username} - NOT FOUND DB")
                raise UserNotFound

            else:
                async with self.session as delete_session:
                    await delete_session.execute(query)
                    await delete_session.commit()

        self.logger.info(f"User {user_data.id} - {self.data.username} - Delete")

        return True

    async def get_user(self) -> GetUserOutput:
        query = sqlalchemy.select(User).where(User.username == self.data.username)

        async with self.session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                self.logger.info(f"User {self.data.username} - NOT FOUND DB")
                raise UserNotFound

            self.logger.info(f"User {user_data.id} - {user_data.username} - SELECT DB")

            return user_data
