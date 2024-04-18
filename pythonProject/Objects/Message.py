class Message:
    """
            Модель объекта сообщения
    """

    def __init__(self, _text):
        self.text = _text

    def get_text(self):
        return self.text
