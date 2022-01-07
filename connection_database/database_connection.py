from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src import settings

conn_str = f'mysql://{settings.USERNAME_DB}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.DB_NAME}'
#conn_str= f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db_name}'
engine_mysql = create_engine(conn_str)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_mysql)

Base = declarative_base()