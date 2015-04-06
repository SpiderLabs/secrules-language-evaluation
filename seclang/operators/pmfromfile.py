
from seclang.sec_operator import SecOperator
import os

class pmfromfile(SecOperator):
    def evaluate(self, input, transaction):
        matches = []
        files = str(self.argument).split(" ")
        for fn in files:
            lines = [line.rstrip('\n') for line in open(os.path.join(self.path, fn))]
            matches = matches + lines

        for t in matches:
            if str(t) in str(input):
                return True

        return False


