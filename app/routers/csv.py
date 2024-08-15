import io
import pandas as pd
from fastapi import APIRouter, UploadFile, File
from app.dependencies.database import engine


router = APIRouter(prefix="/csv", tags=["csv"])


@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    df.to_sql('monitoring_data', engine, if_exists='append', index=False)

    return {"filename": file.filename, "message": "CSV file processed successfully!"}
