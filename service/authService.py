from repository.authRepository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from schema.inputs import RegisterInputs, UpdateUsernameInput, DeleteUserInput
from model.usersModel import User


class UserService:
    def __init__(self, data: RegisterInputs | UpdateUsernameInput | DeleteUserInput, session: AsyncSession):
        self.repository = UserRepository(db_session=session, data=data)

    async def create(self) -> bool:
        await self.repository.create_user()
        return True

    async def update(self) -> User:
        user = await self.repository.update_username()
        return user

    async def delete(self) -> bool:
        status = await self.repository.delete_user()
        return status
