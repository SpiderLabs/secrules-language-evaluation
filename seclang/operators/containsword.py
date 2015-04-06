
from seclang.sec_operator import SecOperator

class containsword(SecOperator):
    def evaluate(self, input, transaction):
        if str(self.argument) == "":
            return True

        if str(self.argument) == str(input):
            return True

        for b in [" ", ">", "<", '\x00']:
            if str(self.argument + b) in str(input):
                return True

            if str(b + self.argument) in str(input):
                return True

        return False

        return str(input).startswith(str(self.argument))

