from sqlalchemy import Column, String, Integer, ForeignKey
from app.connect.extension.extension import db

class UserDB(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False)

    habits = db.relationship('HabitDB', backref='user', lazy='dynamic')
    