from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence, String

from app.db.postpres.base import Base


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, Sequence("issue_id_seq"), primary_key=True)
    name = Column(String(50))
    create_date = Column(DateTime)
    update_date = Column(DateTime)
    color = Column(String(7))
    status = Column(String(20))

    user_id = Column(Integer, ForeignKey("users.id"))
