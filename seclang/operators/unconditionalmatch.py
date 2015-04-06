
from seclang.sec_operator import SecOperator

class unconditionalmatch(SecOperator):
    def evaluate(self, input, transaction):
        if str(self.argument) == "":
            return True
        if str(input) == "":
            return True

        return False

