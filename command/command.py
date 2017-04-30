class Command(object):
    def execute(self):
        raise NotImplementedError("Derive a class from Command and implement the execute() function.")