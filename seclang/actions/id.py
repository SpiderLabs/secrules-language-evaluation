
from seclang.sec_action import SecAction

class id(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#id
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        id = self.action[3:]
        if id[0] == "'":
            id = id[1:-1]
        id = int(id)
        core.id = id
        return id

