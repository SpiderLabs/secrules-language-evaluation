
from seclang.sec_operator import SecOperator

class validatebyterange(SecOperator):
    def evaluate(self, input, transaction):
        num = []

        for i in str(self.argument).split(","):

            if "-" in i:
                s = int(i.split("-")[0])
                e = int(i.split("-")[1])
                while s <= e:
                    num.append(s)
                    s = s + 1
            if i != None and i != "" and not "-" in i:
                try:
                    num.append(int(i))
                except:
                    for i in map(ord, i):
                        num.append(i)

        for c in map(ord, input):
            if not c in num:
                return True

        return False
