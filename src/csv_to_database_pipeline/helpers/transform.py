from fastapi import UploadFile
import pandas as pd
from ..dependencies import get_session
from sqlmodel import select
from contextlib import closing


"""
Transforms CSV data from an uploaded file into a list of TaxiZone objects.

This function reads a CSV file from an UploadFile object, removes any rows
with missing values or duplicate 'LocationID' entries, and filters out
entries that already exist in the database. It then creates and returns
a list of TaxiZone objects for the new entries.

Args:
    file (UploadFile): The uploaded CSV file containing taxi zone data.

Returns:
    List[TaxiZone]: A list of TaxiZone objects representing new entries
    not already present in the database.
"""
def transform_data(file: UploadFile):
    from ..modules import TaxiZone

    file.file.seek(0)
    df = pd.read_csv(file.file)
    df.dropna(inplace=True)

    df.drop_duplicates(subset=["LocationID"], inplace=True)

    with closing(get_session()) as session_gen:
        session = next(session_gen)
        taxi_zones_location_ids = session.scalars(select(TaxiZone.location_id)).all()

    taxi_zones_location_unique_ids = set(taxi_zones_location_ids)
    new_df = df[~df["LocationID"].isin(taxi_zones_location_unique_ids)]

    taxi_zones = []
    for _, row in new_df.iterrows():
        taxi_zone = TaxiZone(
            location_id=row.get("LocationID"),
            borough=row.get("Borough"),
            zone=row.get("Zone"),
            service_zone=row.get("service_zone"),
        )
        taxi_zones.append(taxi_zone)

    return taxi_zones
