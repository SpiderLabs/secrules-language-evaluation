
from seclang.sec_operator import SecOperator

class nomatch(SecOperator):
    def evaluate(self, input, transaction):
        if str(self.argument) == "":
            return False
        if str(input) == "":
            return False

        if str(self.argument) in str(input):
            return False

        return True

