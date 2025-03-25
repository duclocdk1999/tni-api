from datetime import datetime
from sqlmodel import SQLModel


class ImageResponse(SQLModel):
    id: int
    record_time: datetime
    number_of_people: int
    file_name: str
