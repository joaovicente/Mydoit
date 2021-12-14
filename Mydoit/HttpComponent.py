from .Message import Message
import requests

class HttpComponent:
    def produce(self, endpoint, data=None):
        # Make appropriate HTTP call
        if data is None:
            response = requests.get(url=endpoint)
        else:
            response = requests.post(url=endpoint, data=data)
        # Store response content in Message body
        message = Message(response.text)
        # Return message
        return message
