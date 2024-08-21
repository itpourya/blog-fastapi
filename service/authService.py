from repository.authRepository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from schema.inputs import RegisterInputs, UpdateUsernameInput, DeleteUserInput
from schema.outputs import RegisterOutput
from model.usersModel import User
from pkg.jwt import Security


class UserService:
    def __init__(self, data: RegisterInputs | UpdateUsernameInput | DeleteUserInput, session: AsyncSession):
        self.session = session
        self.data = data

    async def create(self) -> RegisterOutput:
        self.data.password = Security.get_password_hash(password=self.data.password)
        repository = UserRepository(data=self.data, db_session=self.session)
        user = await repository.create_user()
        return user

    async def update(self) -> User:
        repository = UserRepository(data=self.data, db_session=self.session)
        user = await repository.update_username()
        return user

    async def delete(self) -> bool:
        repository = UserRepository(data=self.data, db_session=self.session)
        status = await repository.delete_user()
        return status
