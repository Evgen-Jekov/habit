from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from app.connect.extension.extension import db


class HabitDB(db.Model):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    description = Column(String(1024), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    progress = Column(Integer, nullable=False)
    status = Column(String(256), nullable=False)
    goal = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)