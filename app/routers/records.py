from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.dependencies.database import get_db
from app.models.records import Record


router = APIRouter(prefix="/records", tags=["records"])


class RecordRequest(BaseModel):
    equipment_id: str
    timestamp: str
    value: float


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Record).all()


@router.get("/{id}")
def get_by_id(id: str, db: Session = Depends(get_db)):
    return db.query(Record).filter(Record.id == id).all()


@router.post("/")
def create(data: RecordRequest, db: Session = Depends(get_db)):
    request = Record(**data.dict())
    db.add(request)
    db.commit()
    db.refresh(request)

    return request
