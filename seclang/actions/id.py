
from seclang.sec_action import SecActionMetadata

class id(SecActionMetadata):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#id
    """
    def evaluate(self, core):
        id = self.action[3:]
        if id[0] == "'":
            id = id[1:-1]
        id = int(id)
        core.id = id
        return id

