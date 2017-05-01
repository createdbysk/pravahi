import plugins.emitter


class Emitter(plugins.emitter.Emitter):
    def __init__(self):
        super(Emitter, self).__init__()

    def __emit_command(self, **kwargs):
        print "aws emit_command", kwargs
