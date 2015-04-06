
from seclang.sec_operator import SecOperator

class endswith(SecOperator):
    def evaluate(self, input, transaction):
        return str(input).endswith(str(self.argument))

