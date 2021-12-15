from Mydoit import read, write
import os
import shutil
from datetime import datetime

MY_TMP_DIR = 'tmp'

def test_write_file():
    path, test_string = single_test_file_setup()
    assert write(path, test_string) == None
    assert read_file_content(path) == test_string
    single_test_file_teardown()

def test_read_file():
    path, test_string = single_test_file_setup()
    write_file_content(path, test_string)
    assert isinstance(read(path).text(), str)
    single_test_file_teardown()

def test_read_http():
    url = 'https://httpbin.org/get'
    text = read(url).text()
    assert isinstance(text, str)
    assert 'args' in text

def test_read_http_show():
    url = 'https://httpbin.org/get'
    text = read(url).show()

def test_write_http():
    url = 'https://httpbin.org/post'
    data = {"foo":"bar"}
    message = write(url, data)
    text = message.text()
    assert isinstance(text, str)
    assert 'args' in text
    assert message.body.request.method == 'POST'

def test_write_http_put():
    url = 'https://httpbin.org/put'
    data = {"foo":"bar"}
    message = write(url, data, options={"httpMethod":"PUT"})
    text = message.text()
    assert isinstance(text, str)
    assert 'args' in text
    assert message.body.request.method == 'PUT'

def write_file_content(path, content):
    f = open(path, "w+")
    f.write(content)
    f.close()    

def read_file_content(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content

def single_test_file_setup():
    os.makedirs(MY_TMP_DIR, exist_ok=True)
    path = os.path.join(MY_TMP_DIR, 'single_file_test_data.txt')
    test_string = str(datetime.now())
    return path, test_string

def single_test_file_teardown():
    shutil.rmtree(MY_TMP_DIR)

