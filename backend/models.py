from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class Hire(Base):
    __tablename__ = "hire"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    service = Column(String)