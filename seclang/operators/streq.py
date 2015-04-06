
from seclang.sec_operator import SecOperator

class streq(SecOperator):
    def evaluate(self, input, transaction):
        return str(self.argument) == str(input)

