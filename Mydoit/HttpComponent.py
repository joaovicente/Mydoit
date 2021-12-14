from .HttpMessage import HttpMessage
import requests

class HttpComponent:
    def produce(self, endpoint, data=None, options={}):
        # Make appropriate HTTP call
        if data is None:
            response = requests.get(url=endpoint)
        elif options is not None and 'httpMethod' in options and options['httpMethod'] == 'PUT':
            response = requests.put(url=endpoint, data=data)
        else:
            response = requests.post(url=endpoint, data=data)
        # Store response content in Message body
        message = HttpMessage(response)
        # Return message
        return message
