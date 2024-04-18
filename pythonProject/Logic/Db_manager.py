from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Objects.Profile import Profile
from Objects.Session import Session
from random import randint


class Data_base_manadger:
    """
            Модель объекта,отвечающего за работу с базой данных.
    """

    def get_user(self, username):
        """
                :param username type(string)
                :return объект класса Profile
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Profile).filter_by(username=username).first()
        return query

    def upload_messages(self, _username1, _username2):
        """
                    :param _username1 type(string)
                    :param _username2 type(string)
                    :return type(list[string,...,string])
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Session).filter_by(username1=_username1, username2=_username2).first()
        if (query == None):
            query = s.query(Session).filter_by(username1=_username2, username2=_username1).first()
        return query.messages

    def download_message(self, _username1, _username2, message):
        """
                    :param _username1 type(string)
                    :param _username2 type(string)
                    :param message объект класса Message
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Session).filter_by(username1=_username1, username2=_username2).first()
        if (query == None):
            query = s.query(Session).filter_by(username1=_username2, username2=_username1).first()
        messages = query.messages
        data = eval(messages)
        last_item_id = len(data)
        data[last_item_id + 1] = message
        query.messages = str(data)
        s.add(query)
        s.commit()

    def register_user(self, _username, _password):
        """
                    :param _username type(string)
                    :param _password type(string)
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(Profile).filter_by(username=_username).first()
        if (query == None):
            user = Profile(username=_username, password=_password)
            s.add(user)
            s.commit()
        else:
            print("Пользователь с таким именем уже существует")
            return 1

    def register_session(self, _username1, _username2):
        """
                    :param username1 type(string)
                    :param username2 type(string)
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)
        s = session()
        _password = randint(10000000, 1000000000)
        query1 = s.query(Session).filter_by(username1=_username1, username2=_username2).first()
        query2 = s.query(Session).filter_by(username1=_username1, username2=_username2).first()
        if (query1 == None and query2 == None):
            se = Session(username1=_username1, username2=_username2, password=_password, messages="{}")
            s.add(se)
            s.commit()
        else:
            print("Такая сессия уже существует")
            return 1

    def get_session(self, _username1, _username2):
        """
                    :param _username1 type(string)
                    :param _username2 type(string)
                    :return объект класс Session
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        session = sessionmaker(bind=engine)
        s = session()
        if (_username2 == None):
            query = s.query(Session).filter_by(username1=_username1).all()
            if(query!=[]):
                return query
            else:
                query = s.query(Session).filter_by(username2=_username1).all()
                return query
        else:
            query = s.query(Session).filter_by(username1=_username1, username2=_username2).first()
            if (query != None):
                return query
            else:
                if (query != []):
                    return s.query(Session).filter_by(username1=_username2, username2=_username1).first()
                else:
                    print("Такой сессии не существует")
                    return 1

    def sign_in(self, _username):
        """
                    :param _username type(string)
                    :return type(dictionary) (зашифрованный пароль)
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Profile).filter_by(username=_username).first()
        if (query != None):
            return query.password
        else:
            print("Пользователя с таким именем не существет")
            return 1

    def delete_user(self, _username):
        """
                    :param _username type(string)
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Profile).filter_by(username=_username).first()
        if (query != None):
            s.delete(query)
            s.commit()
        else:
            print("Пользователя с таким именем не существет")
            return 1

    def change_password(self, _username, new_password):
        """
                    :param _username type(string)
                    :param new_password type(string)
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Profile).filter_by(username=_username).first()
        if (query != None):
            query.password = new_password
        else:
            print("Пользователя с таким именем не существет")
            return 1

    def change_username(self, _username, new_username):
        """
                    :param _username type(string)
                    :param new_username type(string)
        """
        engine = create_engine('sqlite:///db.db', echo=True)
        session = sessionmaker(bind=engine)
        s = session()
        query = s.query(Profile).filter_by(username=_username).first()
        if (query != None):
            query.username = new_username
        else:
            print("Пользователя с таким именем не существет")
            return 1
