from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

entries = Table(
    'entries',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('content', String, nullable=False)
)
