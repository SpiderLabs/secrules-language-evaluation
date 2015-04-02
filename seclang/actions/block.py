
from seclang.sec_action import SecAction

class block(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#block
    """
    def evaluate(self, core):
        #print " ** Performs what is defined at SecDefaultAction."
        return True

