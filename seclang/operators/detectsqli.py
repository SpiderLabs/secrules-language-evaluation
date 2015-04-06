
from seclang.sec_operator import SecOperator

class detectsqli(SecOperator):
    def evaluate(self, input, transaction):
        try:
            from libinjection import *
            s = sqli_state()
            sqli_init(s, str(input), libinjection.FLAG_QUOTE_NONE | libinjection.FLAG_SQL_ANSI)
            client9 = libinjection.is_sqli(s)
            return client9 == 1
        except:
            raise BaseException("libinjection is not supported")

