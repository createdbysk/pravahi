import plugins.aws.emitter


class Emitter(plugins.aws.emitter):
    def emit_command(self):
        print "aws emit_command"
