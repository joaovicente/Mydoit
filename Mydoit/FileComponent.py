from .Message import Message

class FileComponent:
    def produce(destination, content):
        f = open(destination, "w+")
        f.write(content)
        f.close()

    def consume(source):
        f = open(source, 'r')
        content = f.read()
        f.close()
        return Message(content)
