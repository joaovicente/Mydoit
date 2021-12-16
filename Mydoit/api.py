from Mydoit.ComponentAdapter import ComponentAdapter
from Mydoit.Message import Message
from Mydoit.FileComponent import FileComponent

def write(destination, data, options={}):
    r"""
    Writes data to a destination
    :param data: The data to write
    :param destination: The destination
    """
    return ComponentAdapter().write(destination, data, options)

def read(source):
    r"""
    Reads data from a source
    :param source: The source of data
    :return the Message containing the data
    """
    return ComponentAdapter().read(source)