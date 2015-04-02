
from seclang.sec_action import SecAction

class status(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#status
    """
    def evaluate(self, core):
        #print " ** Specifies the response status code to use with actions deny and redirect."
        return 404

