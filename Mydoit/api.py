from Mydoit.ComponentAdapter import ComponentAdapter
from .Message import Message
from .FileComponent import FileComponent

def write(destination, data):
    r"""
    Writes data to a destination
    :param data: The data to write
    :param destination: The destination
    """
    return ComponentAdapter().write(destination, data)

def read(source):
    r"""
    Reads data from a source
    :param source: The source of data
    :return the Message containing the data
    """
    return ComponentAdapter().read(source)