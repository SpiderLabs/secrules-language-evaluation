
from seclang.sec_action import SecAction

class rev(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#rev
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        a = self.action[4:]
        if a[0] == "'":
            a = a[1:-1]
        core.rev = a
        return a

