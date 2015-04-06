
from seclang.sec_operator import SecOperator

class detectxss(SecOperator):
    def evaluate(self, input, transaction):
        try:
            from libinjection import *
            client9 = libinjection.xss(str(input))
            return client9 == 1
        except:
            raise BaseException("libinjection is not supported")

