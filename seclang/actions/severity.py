
from seclang.sec_action import SecActionMetadata

class severity(SecActionMetadata):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#severity
    """
    def evaluate(self, core):
        a = self.action[9:]
        if a[0] == "'":
            a = a[1:-1]

        if a == "EMERGENCY":
            a = 0
        elif a == "ALERT":
            a = 1
        elif a == "CRITICAL":
            a = 2
        elif a == "ERROR":
            a = 3
        elif a == "WARNING":
            a = 4
        elif a == "NOTICE":
            a = 5
        elif a == "INFO":
            a = 6
        elif a == "DEBUG":
            a = 7

        a = int(a)
        core.severity = a
        return a

