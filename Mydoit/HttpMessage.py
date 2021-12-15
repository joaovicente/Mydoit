from .Message import Message
from . import utils

class HttpMessage(Message):
    def text(self):
        return self.body.text

    def show(self):
        utils.mypprint(self.text())
