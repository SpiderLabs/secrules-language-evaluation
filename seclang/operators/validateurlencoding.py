
from seclang.sec_operator import SecOperator

class validateurlencoding(SecOperator):
    def evaluate(self, input, transaction):
        if str(input) == "":
            return False
        i = 0
        while i < len(str(input)):
            if input[i] == '%':
                if i + 2 >= len(str(input)):
                    return True
                else:
                    c1 = input[i+1]
                    c2 = input[i+2]

                    if ((c1 >= '0' and c1 <= '9') or (c1 >= 'a' and c1 <= 'f') or (c1 >= 'A' and c1 <= 'F')) and ((c2 >= '0' and c2 <= '9') or (c2 >= 'a' and c2 <= 'f') or (c2 >= 'A' and c2 <= 'F')):
                        i = i + 2
                    else:
                        return True

            i = i + 1

        return False


