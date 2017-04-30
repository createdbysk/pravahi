def load():
    """Loads the configuration file named pravahi.conf from the current working directory.

        :return The configuration as a python object."""

    with open("pravahi.conf", mode='r') as fs:
        import json
        conf_json = json.load(fs, encoding='utf-8')
        return conf_json
