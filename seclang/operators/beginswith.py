
from seclang.sec_operator import SecOperator

class beginswith(SecOperator):
    def evaluate(self, input, transaction):
        return str(input).startswith(str(self.argument))

