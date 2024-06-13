from sqlalchemy import create_engine
from app.models import metadata

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
