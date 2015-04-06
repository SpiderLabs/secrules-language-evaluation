
from seclang.sec_operator import SecOperator
import re

class rx(SecOperator):
    def evaluate(self, input, transaction):
        try:
            m = re.search(self.argument, input)
            if m == None:
                return False
            else:
                return True
        except:
            return False


