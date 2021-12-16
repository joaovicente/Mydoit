from Mydoit.Message import Message

class FileComponent:
    def produce(self, endpoint, data):
        f = open(endpoint, "w+")
        f.write(data)
        f.close()

    def consume(self, endpoint):
        f = open(endpoint, 'r')
        data = f.read()
        f.close()
        return Message(data)
