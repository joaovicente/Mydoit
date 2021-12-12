def hello(name):
    return "Hello " + name

def write(content, destination):
    r"""
    Writes content to a destination
    :param content: The string to write
    :param destination: The destination
    """
    f = open(destination, "w+")
    f.write(content)
    f.close()

def read(source):
    r"""
    Reads data from a source
    :param source: The source of data
    :return a string contaning the data
    """
    f = open(source, 'r')
    content = f.read()
    f.close()
    return content

