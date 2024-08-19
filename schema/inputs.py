from pydantic import BaseModel


class RegisterInputs(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class UpdateUsernameInput(BaseModel):
    old_username: str
    new_username: str


class DeleteUserInput(BaseModel):
    username: str
    password: str
