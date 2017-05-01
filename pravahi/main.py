class Main(object):
    def __init__(self):
        import pravahi.conf_loader
        self.conf = pravahi.conf_loader.load()
        self.provider_factory = self.__load_provider()

    def get_command(self, command_name):
        if command_name == 'validate':
            validate_command = self.provider_factory.get_validate_command(self.conf)
            return validate_command

    def execute_command(self, args):
        command = self.get_command(args[1])
        command.execute()

    def __load_provider(self):
        import provider_factory
        if 'provider' in self.conf:
            return provider_factory.get_provider_factory(self.conf['provider'])
        else:
            raise KeyError("provider not found in configuration. Add a provider key-value pair.")

