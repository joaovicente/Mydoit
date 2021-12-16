from Mydoit.Message import Message
from Mydoit import utils

class HttpMessage(Message):
    def text(self):
        return self.body.text

    def show(self):
        utils.mypprint(self.text())
