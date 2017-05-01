import plugins.provider_abstract_factory


class AwsProviderFactory(plugins.provider_abstract_factory.ProviderAbstractFactory):
    """
    The factory for the AWS provider.
    """
    def get_validate_command(self, conf):
        import validate
        return validate.Validate(conf, self)

    def get_emitter(self):
        import emitter
        return emitter.Emitter()
