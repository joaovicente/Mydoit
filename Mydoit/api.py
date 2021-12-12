from .Message import Message
from .FileComponent import FileComponent

def write(destination, data):
    r"""
    Writes data to a destination
    :param data: The data to write
    :param destination: The destination
    """
    return FileComponent.produce(destination, data)

def read(source):
    r"""
    Reads data from a source
    :param source: The source of data
    :return the Message containing the data
    """
    return FileComponent.consume(source)
