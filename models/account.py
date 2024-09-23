from sqlalchemy import Column, Integer, String

from models.init import Base

class Account(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, foreign_key=True, nullable=False)
    username = Column(String)
    locale = Column(String, nullable=True)