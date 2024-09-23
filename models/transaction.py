from sqlalchemy import Column, Integer, String

from models.init import Base

class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)