import command


class Validate(command.Command):
    """
    Implements the validate command.
    """
    def __init__(self, conf):
        self.conf = conf

    def execute(self):
        print self.conf