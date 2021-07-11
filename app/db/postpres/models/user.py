from sqlalchemy import Column, DateTime, Integer, String

from app.db.postpres.postpresdatabase import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(200))
    username = Column(String(50))
    email = Column(String(50))
    phone = Column(String(13))
    password = Column(String(100))
    date_of_birth = Column(DateTime)
    bio = Column(String(100))
    gender = Column(String(20))
