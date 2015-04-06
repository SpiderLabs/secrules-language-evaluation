
from seclang.sec_operator import SecOperator

class validateutf8encoding(SecOperator):
    def evaluate(self, input, transaction):
        if input == "":
            return False

        try:
            a = input.encode('raw-unicode-escape').decode('ISO-8859-1')
            a = input.encode('raw-unicode-escape').decode('utf-8')
        except:
            return True

        return False

