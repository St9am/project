from Logic.Db_manager import Data_base_manadger
from Objects.Cryptor import Cryptor


class Profile_manager:
    """
            Модель объекта,отвечающего за работу с профилем
    """

    def register(self):
        db_manager = Data_base_manadger()
        username = input()
        password = input()
        cryptor = Cryptor()
        encrypted_password = cryptor.hash_password(password)
        db_manager.register_user(username, str(encrypted_password))

    def change_username(self, username, new_username):
        """
                    :param username type(string)
                    :param new_username type(string)
        """
        db_manager = Data_base_manadger()
        db_manager.change_username(username, new_username)

    def change_password(self, username, new_password):
        """
                    :param username type(string)
                    :param new_password type(string)
        """
        db_manager = Data_base_manadger()
        db_manager.change_password(username, new_password)

    def delete_profile(self,username):
        """
                    :param username type(string)
        """
        db_manager = Data_base_manadger()
        db_manager.delete_user(username)

    def get_password(self, username):
        """
                    :param username type(string)
        """
        db_manager = Data_base_manadger()
        return db_manager.get_user(username).password

    def sign_in(self, username, password):
        """
                    :param username type(string)
                    :param password type(string)
                    :return type(Boolean)
        """
        db_manager = Data_base_manadger()
        encrypted_password = db_manager.sign_in(username)
        cryptor = Cryptor()
        return cryptor.check_password(encrypted_password, password)
