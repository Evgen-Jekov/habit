from flask_sqlalchemy import SQLAlchemy
from flask import Flask


client_sql = SQLAlchemy()




def connect_extension(app : Flask) -> None:
    client_sql.init_app(app)