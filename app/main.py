import uvicorn
from fastapi import FastAPI
from app.routers import csv, records
from app.dependencies.cors import init_cors

app = FastAPI()

init_cors(app)

app.include_router(records.router)
app.include_router(csv.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
