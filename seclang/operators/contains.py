
from seclang.sec_operator import SecOperator

class contains(SecOperator):
    def evaluate(self, input, transaction):
        if str(self.argument) == "":
            return True

        if str(self.argument) in str(input):
            return True

        return False

