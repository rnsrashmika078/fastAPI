from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post("/blog")
def create(request: schemas.Blog):
    return {
        "result": {
            "message": "post created successfully!",
            "title": request.title,
            "body": request.body,
        },
    }
