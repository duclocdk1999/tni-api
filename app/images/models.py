from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Image(SQLModel, table=True):
    __tablename__ = "images_image"

    id: int = Field(primary_key=True, default=None, nullable=False)
    record_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=True)
    image_path: str = Field(default="", nullable=False)
    number_of_people: int = Field(default=0)
