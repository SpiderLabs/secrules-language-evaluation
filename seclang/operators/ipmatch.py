
from seclang.sec_operator import SecOperator
from seclang.sec_log import *

class ipmatch(SecOperator):
    def evaluate(self, input, transaction):
        try:
            import ipaddress
        except:
            raise BaseException("ipaddress is not supported")

        try:
            return ipaddress.ip_address(unicode(input)) in ipaddress.ip_network(unicode(self.argument), strict=False)
        except:
            return False

