
from seclang.sec_operator import SecOperator

class strmatch(SecOperator):
    def evaluate(self, input, transaction):
        for c in str(self.argument).split("|"):
            if str(c) in str(input):
                return True
        return False
