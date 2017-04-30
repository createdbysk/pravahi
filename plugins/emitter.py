class Emitter(object):
    """
    The base class for emitters.
    """
    def emit_command(self, **kwargs):
        """

        :param kwargs: {"name": "The name of the step", "command": "The command to execute"}
        :return: None
        """
        raise NotImplementedError("Derive a class from Command and implement the emit_command() function.")