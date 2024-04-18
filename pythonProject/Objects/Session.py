from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.db', echo=True)
Base = declarative_base()


class Session(Base):
    """
            Модель таблицы базы данных в виде класса
    """
    __tablename__ = 'Sessions'
    id = Column(Integer, primary_key=True)
    username1 = Column(Integer)
    username2 = Column(Integer)
    password = Column(Integer)
    messages = Column(String)
