

class SecInclude():
    def __init__(self, filename):
        self.filename = filename

    def evaluate(self, core):
        rules = ""
        with open(self.filename) as f:
            rules = f.read().splitlines()
        core.include(rules)


class SecConfig():
    def __init__(self, config, value):
        self.config = config
        self.value = value

    def evaluate(self, core):
        setattr(core, self.config, self.value)


