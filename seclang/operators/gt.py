
from seclang.sec_operator import SecOperator

class gt(SecOperator):
    def evaluate(self, input, transaction):
        return self.t_int(input) > self.t_int(self.argument)


