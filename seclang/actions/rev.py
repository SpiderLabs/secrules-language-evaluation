
from seclang.sec_action import SecActionMetadata

class rev(SecActionMetadata):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#rev
    """
    def evaluate(self, core):
        a = self.action[4:]
        if a[0] == "'":
            a = a[1:-1]
        core.rev = a
        return a

