from fastapi import FastAPI, HTTPException
from typing import Optional
from src.schemas import PostCreate
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(
    title="Twitter Clone API",
    description="This is a sample twitter clone fastapi application",
    version="1.0.0"
)


# temporary database
text_posts = {
    "1": {
        "title": "Post 01",
        "content": "This is my first post"
    },
    "2": {
        "title": "Post 02",
        "content": "This is my second post"
    },
    "3": {
        "title": "Post 03",
        "content": "This is my third post"
    },
    "4": {
        "title": "Post 04",
        "content": "This is my fourth post"
    },
    "5": {
        "title": "Post 05",
        "content": "This is my fifth post"
    }
}


#---------------------------------------- API ROUTES ----------------------------------------#


#homepage
@app.get("/")
def homepage():
    return "Welcome to twitter clone homepage !!"


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