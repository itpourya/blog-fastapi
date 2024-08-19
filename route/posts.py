from fastapi import APIRouter

post_router: APIRouter = APIRouter()


@post_router.get("/posts")
async def show_posts():
    ...


@post_router.post("/create_posts")
async def create_post():
    ...


@post_router.get("/detail/posts")
async def posts_detail():
    ...


@post_router.put("/update_posts")
async def update_posts():
    ...


@post_router.delete("/delete_posts")
async def delete_posts():
    ...