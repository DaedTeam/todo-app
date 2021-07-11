from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, Sequence, String, Text
)

from app.db.postpres.base import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, Sequence("note_id_seq"), primary_key=True)
    title = Column(String(50))
    detail = Column(Text)
    color = Column(String(7))
    create_date = Column(DateTime)
    update_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
