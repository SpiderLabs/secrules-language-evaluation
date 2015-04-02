

from sec_operator import *
from sec_log import *

class SecRule():
    def __init__(self, directive, input, operator, action, rule, line, filename):

        if not isinstance(operator, SecOperator):
            operator = SecOperator("@pm " + operator)

        self.directive = directive
        self.input = input
        self.operator = operator
        self.action = action
        self.line = line
        self.filename = filename
        self.rule = rule

        self.phase = 2
        self.id = None

        if action != None:
            for a in action:
                if a.pre_process == True:
                    a.evaluate(self)

    def __str__(self):
        rule = "Rule: " + str(self.directive) + " " + \
            str(self.input) + " " + \
            str(self.operator) + " " + \
            str(self.action) + " @" + \
            str(self.filename) + ":" + str(self.line)
            
        return rule

    def evaluate(self, http_transaction):

        debug_log(4, "Executing operator \"" + str(self.operator.name) + "\" with param \"" +
                str(self.operator.argument) + "\" against " + str(self.input) + ".")

        self.input.setTransaction(http_transaction)
        input_value = self.input.content()

        debug_log(9, "Target value: \"" + str(input_value) + "\"")

        res = self.operator.evaluate(self.input, http_transaction)
        return res

