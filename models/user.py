from sqlalchemy import Column, Integer, String

from models.init import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String)
    locale = Column(String, nullable=True)