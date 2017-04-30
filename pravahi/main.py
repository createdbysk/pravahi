class Main(object):
    def __init__(self):
        import pravahi.conf_loader
        self.conf = pravahi.conf_loader.load()
        self.provider = self.load_provider()

    def get_command(self, command_name):
        if command_name == 'validate':
            import command.validate

            validate_command = command.validate.Validate(self.conf)
            return validate_command

    def execute_command(self, args):
        command = self.get_command(args[1])
        command.execute()

    def load_provider(self):
        import provider_factory
        if self.conf.has_key('provider'):
        else:
            raise
        provider_name = self.conf['']
