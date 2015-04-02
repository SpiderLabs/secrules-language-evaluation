
from seclang.sec_action import SecAction

class deny(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#deny
    """
    def evaluate(self, core):
        #print " ** Stops rule processing and intercept the transaction."
        return True

