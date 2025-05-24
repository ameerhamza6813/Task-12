from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, schemas
from s3_utils import upload_csv_to_s3

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos", response_model=schemas.TodoOut)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos", response_model=List[schemas.TodoOut])
def list_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@app.put("/todos/{id}", response_model=schemas.TodoOut)
def update_todo(id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).get(id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).get(id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}

@app.get("/export")
def export_csv(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    url = upload_csv_to_s3(todos)
    return {"csv_url": url}
