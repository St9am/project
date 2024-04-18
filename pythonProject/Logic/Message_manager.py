from Objects.Cryptor import Cryptor
from Logic.Db_manager import Data_base_manadger


class Message_manager:
    """
        Модель класса,отвечающего за работу с сообщениями(отправку,получение,шифровку)
    """

    def message(self, username1, username2, _message):
        """
                    :param username1 type(string)
                    :param username2 type(string)
                    :param _message объект класса Message
        """
        cryptor = Cryptor()
        password = username1.get_session_password(username2)
        encrypted_message = cryptor.encrypt(_message.get_text(), password)
        db_manager = Data_base_manadger()
        db_manager.download_message(username1.get_username(), username2, encrypted_message)

    def get_messages(self, username1, username2, password):
        """
                    :param username1 type(string)
                    :param username2 type(string)
                    :param password type(Integer)
                    :return type(list)
        """
        cryptor = Cryptor()
        db_manager = Data_base_manadger()
        data = eval(db_manager.upload_messages(username1, username2))
        decrypted_messages = []
        for i in range(1, len(data) + 1):
            decrypted_messages.append(cryptor.decrypt(data[i], str(password)))
        return decrypted_messages
