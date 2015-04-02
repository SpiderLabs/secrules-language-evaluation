
from seclang.sec_action import SecAction

class transformation_none(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#log
    """
    def evaluate(self, core):
        #print " ** LOG should goes to the apache error log and audit log"
        return True

