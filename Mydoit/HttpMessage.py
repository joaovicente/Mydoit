from .Message import Message

class HttpMessage(Message):
    def text(self):
        return self.body.text

    def show(self):
        print(self.body.text)