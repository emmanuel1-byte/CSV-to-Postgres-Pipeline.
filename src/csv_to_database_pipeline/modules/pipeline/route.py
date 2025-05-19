from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from fastapi import UploadFile
from ...dependencies import FileValidator, get_session
from sqlmodel import Session
from ...helpers import transform_data

pipeline = APIRouter(prefix="/api/v1/pipeline", tags=["pipeline"])




"""
Handles the POST request to upload a CSV file and store its data in the database.

This endpoint validates the uploaded CSV file, transforms its data into TaxiZone
objects, and adds them to the database session. Duplicate records based on
LocationID are ignored. After committing the session, it returns a JSON response
indicating the number of new records loaded.

Parameters:
    session (Session): Database session dependency.
    file (UploadFile): The uploaded CSV file.
    validate_file (UploadFile): Validated CSV file dependency.

Returns:
    JSONResponse: A response with a message indicating the number of new records
    loaded and a status code of 200.
"""
@pipeline.post("/")
def csv_to_database(
    session: Annotated[Session, Depends(get_session)],
    file: UploadFile,
    validate_file: Annotated[UploadFile, Depends(FileValidator)],
):
    taxi_zones = transform_data(file)

    session.add_all(taxi_zones)
    session.commit()
    return JSONResponse(
        content={
            "message": f"{len(taxi_zones)} New Record loaded. (duplicate ignored)"
        },
        status_code=200,
    )
