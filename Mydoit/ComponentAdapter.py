from Mydoit.FileComponent import FileComponent
from Mydoit.HttpComponent import HttpComponent

def resolve_component(endpoint):
    component = None
    if endpoint.startswith('http://') or endpoint.startswith('https://'):
        component = HttpComponent()
    else:
        component = FileComponent()
    return component

class ComponentAdapter:
    def write(self, destination, data):
        message = None
        component = resolve_component(destination)
        if isinstance(component, FileComponent):
            component.produce(destination, data)
        elif isinstance(component, HttpComponent):
            message = component.produce(destination, data)
        return message

    def read(self, source):
        message = None
        component = resolve_component(source)
        if isinstance(component, FileComponent):
            message = component.consume(source)
        elif isinstance(component, HttpComponent):
            message = component.produce(source)
        return message

