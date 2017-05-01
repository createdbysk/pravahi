class Emitter(object):
    """
    The base class for emitters.
    """
    def __init__(self):
        self.emitters = {
            'command': self.__emit_command
        }

    def emit(self, conf):
        steps = conf['steps']
        for step in steps:
            step_type = step['type']
            emitter = self.emitters[step_type]
            emitter(**step)

    def __emit_command(self, **kwargs):
        """

        :param kwargs: {"name": "The name of the step", "command": "The command to execute"}
        :return: None
        """
        raise NotImplementedError("Derive a class from Command and implement the emit_command() function.")