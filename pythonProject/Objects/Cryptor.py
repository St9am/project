from base64 import b64encode, b64decode
import hashlib
import uuid
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


class Cryptor:
    """
        Модель объекта,шифруещего,расшифровываещего данные по стандарту AES,хешируещего данные по стандарту SHA256.
    """

    def encrypt(self, text, password):
        """
                :param text type(string)
                :param password type(string)
                :return type(bytes)
        """
        data = self.generate_private_key(str(password))
        private_key = data[0]
        salt = data[1]
        cipher_config = AES.new(private_key, AES.MODE_GCM)
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(text, 'utf-8'))
        return {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8')
        }

    def decrypt(self, enc_dict, password):
        """
                :param enc_dict type(bytes)
                :param password type(string)
                :return type(string)
        """
        salt = b64decode(enc_dict['salt'])
        cipher_text = b64decode(enc_dict['cipher_text'])
        nonce = b64decode(enc_dict['nonce'])
        tag = b64decode(enc_dict['tag'])
        private_key = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted.decode("utf-8")

    def generate_private_key(self, password):
        """
                :param password type(string)
                :return type(list[type(string),type(string)])
        """
        salt = get_random_bytes(AES.block_size)
        private_key = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
        return private_key, salt

    def hash_password(self, password):
        """
                :param password type(string)
                :return type(string)
        """
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, hashed_password, user_password):
        """
                :param hashed_password type(string)
                :param user_passwordpassword type(string)
                :return type(Bollean)
        """
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
