from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate


client_alemic = Migrate()
db = SQLAlchemy()



def connect_extension(app : Flask) -> None:
    db.init_app(app)
    client_alemic.init_app(app, db)