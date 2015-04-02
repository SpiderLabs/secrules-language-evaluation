
from seclang.sec_action import SecAction

class allow(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#allow
    """
    def evaluate(self, core):
        return True

