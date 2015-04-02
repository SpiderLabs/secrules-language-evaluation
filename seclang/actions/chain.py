
from seclang.sec_action import SecActionMetadata

class chain(SecActionMetadata):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#chain
    """
    def evaluate(self, core):
        core.chained = True

