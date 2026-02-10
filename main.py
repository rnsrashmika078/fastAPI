from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# http://127.0.0.1:8000/blog?limit=1022&published=true
@app.get("/blog")  # query parameter routes ( query params )
def get_all_blogs(limit: int = 10, published: bool = False, sort: Optional[str] = None):
    return {"blogs": f"{limit} blogs from the db where blog published {published}"}


@app.get("/blog/{id}")  # path parameter route ( dynamic route ) ( path params )
def get_single_blog(id: int):
    return {"blogs": id}


@app.get("/blog/{id}/comments")
def get_blog_post_comment(id: int):
    return {"blogs": {1: "hi", 2: "hello"}}


class Blog(BaseModel):
    title: str
    body: Optional[str]
    published_at: Optional[bool]


@app.post("/blog")
def create_blog_post(request: Blog):
    return {"status": {"message": f"Blog is created with the title as {request.title}"}}
