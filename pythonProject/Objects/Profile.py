from sqlalchemy import Column, Integer, Unicode, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.db', echo=True)
Base = declarative_base()


class Profile(Base):
    """
             Модель таблицы базы данных в виде класса
    """
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode)
    password = Column(String)
