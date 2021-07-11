from sqlalchemy import Column, ForeignKey, Integer, Sequence, String

from app.db.postpres.postpresdatabase import Base


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, Sequence("label_id_seq"), primary_key=True)
    name = Column(String(50))
    color = Column(String(7))
    user_id = Column(Integer, ForeignKey("users.id"))
