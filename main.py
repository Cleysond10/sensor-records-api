import io
import uvicorn
import pandas as pd
from fastapi import Depends, FastAPI, UploadFile, File
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from cors import init_cors
from models import Record

app = FastAPI()

init_cors(app)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class RecordRequest(BaseModel):
    equipment_id: str
    timestamp: str
    value: float


@app.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Record).all()


@app.get("/{id}")
def get_by_id(id: str, db: Session = Depends(get_db)):
    return db.query(Record).filter(Record.id == id).all()


@app.post("/")
def create(data: RecordRequest, db: Session = Depends(get_db)):
    request = Record(**data.dict())
    db.add(request)
    db.commit()
    db.refresh(request)

    return request


@app.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    df.to_sql('monitoring_data', engine, if_exists='append', index=False)

    return {"filename": file.filename, "message": "CSV file processed successfully!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
