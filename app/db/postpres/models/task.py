from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, Sequence, String, Text
)

from app.db.postpres.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, Sequence("task_if_seq"), primary_key=True)
    title = Column(String(50))
    detail = Column(Text)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    color = Column(String(7))
    status = Column(String(20))

    issue_id = Column(Integer, ForeignKey("issues.id"))
