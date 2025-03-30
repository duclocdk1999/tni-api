from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from urllib.parse import quote
import os

# Load environment variables
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{quote(POSTGRES_PASSWORD)}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo=True)

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session
