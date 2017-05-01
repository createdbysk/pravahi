from plugins import command


class Validate(command.Command):
    """
    Implements the validate command.
    """
    def __init__(self, conf, provider_factory):
        self.conf = conf
        self.provider_factory = provider_factory

    def execute(self):
        emitter = self.provider_factory.get_emitter()
        print self.conf
        emitter.emit(self.conf)