from Logic.Message_manager import Message_manager
from Objects.Message import Message
from Logic.Profile_manager import Profile_manager
from Logic.Session_manager import Session_manager


class User:
    """
            Модель объекта пользователя
    """

    def __init__(self):
        self.username = None
        self.password = None
        self.signed_in = False


    def register(self):
        profile_manager = Profile_manager()
        profile_manager.register()

    def start_new_session(self, username):
        """
                    :param username type(string)
        """
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            session_manager = Session_manager()
            if (session_manager.get_session(self.username, username) != 1):
                error = "Такая сессия уже существует"
                return error
            else:
                session_manager.start_new_session(self.username, username)

    def message(self, username, text):
        """
                    :param username type(string)
                    :param text type(string)
        """
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            message = Message(self.username + ": " + text)
            message_manager = Message_manager()
            message_manager.message(self, username, message)

    def get_messages(self, username):
        """
                    :param username type(string) (сообщения от пользователя username)
                    :return type(list[string,string....])
        """
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            message_manadger = Message_manager()
            password = self.get_session_password(username)
            encrypted_mesages = message_manadger.get_messages(self.get_username(), username, password)
            return encrypted_mesages

    def get_session_password(self, username):
        """
                    :param username type(string)
                    :return type(integer)
        """
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            session = self.get_session(username)
            return session.password

    def get_session(self, username):
        """
                    :param username type(string)
                    :return  объект класса Session (сессия пользователя с username)
        """
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            session_manadger = Session_manager()
            session = session_manadger.get_session(self.username, username)
            return session

    def get_sessions(self):
        """
                    :return  type(list[string,...])
        """
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            session_manadger = Session_manager()
            sessions = session_manadger.get_session(self.username)
            data = []
            for i in sessions:
                if (self.get_username() == i.username1):
                    data.append(i.username2)
                else:
                    data.append(i.username1)
            return data

    def sign_in(self, username, password):
        """
                    :param username type(string)
                    :param password type(string)
        """
        profile_manager = Profile_manager()
        signed_in = profile_manager.sign_in(username, password)
        self.signed_in = signed_in
        if (signed_in):
            print("вы вошли в аккаунт")
            self.username = username
            self.password = password
        else:
            print("неверный пароль")

    def get_username(self):
        """
                    :return  type(string)
        """
        return self.username

    def delete_user(self):
        if (self.get_username() == None):
            print("вы не вошли в аккаунт")
        else:
            profile_manager = Profile_manager()
            username = self.get_username()
            profile_manager.delete_profile(username)
            del self
            print("профиль удален")
