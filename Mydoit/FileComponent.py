from .Message import Message

class FileComponent:
    def produce(self, destination, content):
        f = open(destination, "w+")
        f.write(content)
        f.close()

    def consume(self, source):
        f = open(source, 'r')
        content = f.read()
        f.close()
        return Message(content)
