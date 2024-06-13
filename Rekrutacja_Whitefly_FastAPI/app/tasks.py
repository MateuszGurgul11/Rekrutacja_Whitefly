from app.celery_app import celery_app
from app.database import database
from app.models import entries
from sqlalchemy import insert

@celery_app.task
def add_entry_async(title: str, content: str):
    query = insert(entries).values(title=title, content=content)
    database.execute(query)