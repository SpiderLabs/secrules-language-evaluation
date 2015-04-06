
from seclang.sec_operator import SecOperator

class within(SecOperator):
    def evaluate(self, input, transaction):
        if str(self.argument) == "":
            return False
        if str(input) == "":
            return True

        if str(input) in str(self.argument):
            return True

        return False

