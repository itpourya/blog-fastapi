from sqlalchemy.ext.asyncio import AsyncSession
from model.usersModel import User
from schema.inputs import RegisterInputs, UpdateUsernameInput
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy


class UserRepository:
    def __init__(self, data: RegisterInputs | UpdateUsernameInput, db_session: AsyncSession):
        self.session = db_session
        self.data = data

    async def create_user(self):
        user = User(username=self.data.username, password=self.data.password, first_name=self.data.first_name,
                    last_name=self.data.last_name, active=True, email=self.data.email)

        async with self.session as session:
            session.add(user)
            await session.commit()

    async def update_username(self) -> User:
        query = sqlalchemy.select(User).where(User.username == self.data.old_username)
        update_query = sqlalchemy.update(User).where(User.username == self.data.old_username).values(
            username=self.data.new_username)
        async with self.session as session:
            user_data = await session.scalar(query)

            if user_data is None:
                raise ValueError("User not found")

            await session.execute(update_query)
            await session.commit()
            user_data.username = self.data.new_username
            return user_data

    def delete_user(self):
        ...
