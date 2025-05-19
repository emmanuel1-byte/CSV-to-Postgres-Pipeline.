from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
from ..modules import TaxiZone


load_dotenv()

import os

engine = create_engine(os.getenv("DATABASE_URI"), pool_size=5)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


