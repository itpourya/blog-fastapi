from pydantic import BaseModel
from uuid import UUID


class RegisterOutput(BaseModel):
    username: str
    id: UUID


class GetUserOutput(BaseModel):
    username: str
    id: UUID
    first_name: str
    last_name: str
    password: str
    active: bool
    email: str


class JWTPayload(BaseModel):
    username: str
    email: str
    id: str
    exp: int
