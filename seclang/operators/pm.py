
from seclang.sec_operator import SecOperator
from seclang.sec_log import *

class pm(SecOperator):
    def evaluate(self, input, transaction):
        for c in str(self.argument).split("|"):
            for c2 in c.split(" "):
              if str(c2) in str(input):
                  return True

        return False

