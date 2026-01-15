from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import Optional
from src.schemas import PostCreate
from src.temp_db import text_posts
from src.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from dotenv import load_dotenv
load_dotenv()


# lifespan context manager for database setup and teardown
# setup/teardown operations
@asynccontextmanager
async def lifespan(app: FastAPI):
    # create database and tables on startup
    await create_db_and_tables()
    yield
    # any code after yield runs when the app shuts down


app = FastAPI(
    lifespan=lifespan,
    title="Twitter Clone API",
    description="This is a sample twitter clone fastapi application",
    version="1.0.0"
)


# temporary database
text_posts = text_posts


#---------------------------------------- API ROUTES ----------------------------------------#


#homepage
@app.get("/", response_class = HTMLResponse)
def homepage():
    return """
    <html>
        <head>
            <title>Twitter Clone</title>
        </head>
        <body>
            <h1>Welcome to Twitter Clone Application</h1>
        </body>
    </html>
    """
    # Alternatively, you can return plain text return "Welcome to twitter clone homepage !!"


#get all posts
@app.get("/posts")
def get_all_posts(limit: Optional[int] = None):
    if limit:
        return list(text_posts.items())[0:limit]
    else:
        return text_posts


#get a single post by id
@app.get("/posts/{post_id}")
def get_post(post_id: str):
    post = text_posts.get(post_id, None)    # .get() dictionary method, doesn't throw key error if key not found
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")


#create new post
@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[str(len(text_posts) + 1)] = new_post
    return new_post