from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
import os

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['result_backend'],
        broker=app.config['broker_url']
    )
    celery.conf.update(app.config)
    return celery

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or "1f928c700b0b38f415fdb55f90210c6ece0b2103858354dc"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['broker_url'] = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
app.config['result_backend'] = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
celery = make_celery(app)

from . import view, models
