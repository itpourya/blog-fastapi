from fastapi import APIRouter, Body, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from schema.inputs import RegisterInputs, UpdateUsernameInput, DeleteUserInput
from database.engine import get_db
from service.authService import UserService

user_router: APIRouter = APIRouter()


@user_router.post("/signup")
async def signup(db_session: Annotated[AsyncSession, Depends(get_db)], data: RegisterInputs = Body()):
    service = UserService(data=data, session=db_session)
    status = await service.create()
    return status


@user_router.post("/signin")
async def signin():
    ...


@user_router.put("/update")
async def update(db_session: Annotated[AsyncSession, Depends(get_db)], data: UpdateUsernameInput = Body()):
    service = UserService(data=data, session=db_session)
    user = await service.update()
    return user


@user_router.delete("/delete")
async def delete(db_session: Annotated[AsyncSession, Depends(get_db)], data: DeleteUserInput = Body()):
    service = UserService(data=data, session=db_session)
    status = await service.delete()

    return status
