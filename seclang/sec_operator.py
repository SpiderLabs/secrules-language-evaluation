
import urllib
import os
import re

class SecOperator():
    def __init__(self, operator, config=None):
        self.operator = operator
        self.name = self.operator.split(" ")[0][1:]

        self.argument = ' '.join(self.operator.split(" ")[1:])


        self.path = None
        if config != None:
            self.path = os.path.dirname(config)


    def __str__(self):
        return "Operator: " + str(self.operator)


    def evaluate(self, variable, transaction):
        raise BaseException("Operator not implemented")


    def t_int(self, thing):
        try:
            thing = int(thing)
        except:
            thing = 0

        return thing


