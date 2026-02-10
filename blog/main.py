from fastapi import FastAPI, Depends
from . import schemas, model
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/blog")
def get_all_post(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs


@app.post("/blog")
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = model.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {
        "result": {
            "message": "post created successfully!",
            "title": request.title,
            "body": request.body,
        },
    }
