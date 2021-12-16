from Mydoit import utils
class Message:
    def __init__(self, body):
        self.body = body

    def text(self):
        return self.body

    def show(self):
        utils.mypprint(self.body)