
from seclang.sec_action import SecAction

class skip(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#skip
    """
    def evaluate(self, core):
        skip = self.action[5:]
        if skip[0] == "'":
            skip = skip[1:-1]
        skip = int(skip)
        return skip

