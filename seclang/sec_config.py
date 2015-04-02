
import os

class SecInclude():
    def __init__(self, filename, current_config_file):
        base = os.path.dirname(current_config_file)
        self.filename = os.path.join(base, filename)

    def evaluate(self, core):
        rules = ""

        with open(self.filename) as f:
            rules = f.read().splitlines()
        core.include(rules, self.filename)


class SecConfig():
    def __init__(self, config, value):
        self.config = config
        self.value = value

    def evaluate(self, core):
        setattr(core, self.config, self.value)


