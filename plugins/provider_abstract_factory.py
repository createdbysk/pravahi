class ProviderAbstractFactory(object):
    """
    The abstract factory for providers.
    """
    def get_validate_command(self):
        raise NotImplementedError("Derive a class from ProviderAbstractFactory and implement the "
                                  "get_validate_command() function.")

    def get_emitter(self):
        raise NotImplementedError("Derive a class from ProviderAbstractFactory and implement the "
                                  "get_emitter() function.")
