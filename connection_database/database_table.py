from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, LargeBinary
from sqlalchemy.sql.sqltypes import DateTime

from .database_connection import Base

class User(Base):
    
    __tablename__ = "portfolio_test_123"
     
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    name = Column(String(30))
    email = Column(String(30))
    phone = Column(String(12))
    twitter_user = Column(String(30))
    image = Column(String(250))
    text_description = Column(String(250))
    