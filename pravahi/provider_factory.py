def get_provider_factory(provider_name):
    if provider_name == 'aws':
        import plugins.aws.provider_factory
        return plugins.aws.provider_factory.AwsProviderFactory()
    else:
        raise NotImplementedError("%s provider not found."%(provider_name,))
