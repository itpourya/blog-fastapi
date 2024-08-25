from repository.authRepository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from schema.inputs import RegisterInputs, UpdateUsernameInput, DeleteUserInput, LoginInput
from schema.outputs import RegisterOutput
from model.usersModel import User
from pkg.jwtAuth import Security
from pkg.jwtAuth import Token
from fastapi import HTTPException, status


class UserService:
    def __init__(self, data: RegisterInputs | UpdateUsernameInput | DeleteUserInput | LoginInput,
                 session: AsyncSession):
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

    async def login(self) -> Token:
        repository = UserRepository(data=self.data, db_session=self.session)
        user_data = await repository.get_user()
        if Security.verify_password(self.data.password, user_data.password):

            information_token = {
                'id': str(user_data.id),
                'username': user_data.username,
                'email': user_data.email
            }
            token = Security.create_access_token(data=information_token)

            return Token(access_token=token, token_type="bearer")
        else:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
