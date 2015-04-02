
from seclang.sec_action import SecAction

class chain(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#chain
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        core.chained = True

