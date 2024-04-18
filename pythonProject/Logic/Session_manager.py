from Logic.Db_manager import Data_base_manadger


class Session_manager:
    """
            Модель объекта,отвечающего за работу с сессиями
    """

    def start_new_session(self, username1, username2):
        """
                :param username1 type(string)
                :param username2 type(string)

        """
        db_manager = Data_base_manadger()
        db_manager.register_session(username1, username2)

    def get_session(self, username1, username2=None):
        """
                :param username1 type(string)
                :param username2 type(string)(в зависимости передан ли параметр или нет,возвратятся либо все сессии username1, либо сессия username1 c username2)
        """
        db_manager = Data_base_manadger()
        session = db_manager.get_session(username1, username2)
        return session
