
from seclang.sec_action import SecActionMetadata
 
class msg(SecActionMetadata):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#msg
    """
    def evaluate(self, core):
        a = self.action[4:]
        if a[0] == "'":
            a = a[1:-1]
        core.msg = a
        return a

