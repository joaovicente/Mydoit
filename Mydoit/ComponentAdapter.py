from Mydoit.FileComponent import FileComponent

def resolve_component(endpoint):
    return FileComponent()

class ComponentAdapter:
    def write(self, destination, data):
        component = resolve_component(destination)
        if isinstance(component, FileComponent):
            component.produce(destination, data)

    def read(self, source):
        message = None
        component = resolve_component(source)
        if isinstance(component, FileComponent):
            message = component.consume(source)
        return message

