from fastapi import FastAPI
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from src.csv_to_database_pipeline import create_db_and_tables, pipeline
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield



app = FastAPI(
    title="CSV to Postgres Pipeline",
    summary="This is a data pipeline project that accepts CSV files, cleans the data by removing duplicate records, and loads the unique entries into the database. The pipeline ensures data integrity by preventing duplicate storage and provides a streamlined process for CSV data ingestion.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(pipeline)


@app.get("/", tags=["Health"])
def health_check():
    return JSONResponse(
        content={"message": "Static pipeline is active"}, status_code=200
    )
