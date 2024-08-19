from route.users import user_router
from route.posts import post_router
from fastapi import APIRouter

app_router: APIRouter = APIRouter()

app_router.include_router(router=user_router, prefix="/auth")
app_router.include_router(router=post_router, prefix="/posts")
