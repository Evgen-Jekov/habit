from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from app.model.habit import HabitDB
from app.model.user import UserDB


db = SQLAlchemy()
client_alemic = Migrate()



def connect_extension(app : Flask) -> None:
    db.init_app(app)
    client_alemic.init_app(app, db)