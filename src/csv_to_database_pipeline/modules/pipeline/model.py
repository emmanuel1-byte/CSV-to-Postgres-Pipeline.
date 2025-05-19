from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from datetime import datetime, timezone


class TaxiZone(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    location_id: int = Field(nullable=False)
    borough: str = Field(nullable=False)
    zone: str = Field(nullable=False)
    service_zone: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc), nullable=False
    )
