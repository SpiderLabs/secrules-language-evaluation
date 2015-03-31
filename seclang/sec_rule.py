

from sec_operator import *


class SecRule():
    def __init__(self, directive, variable, operator, action, rule, line, filename):

        if not isinstance(operator, SecOperator):
            operator = SecOperator("@pm " + operator)

        self.directive = directive
        self.variable = variable
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
            str(self.variable) + " " + \
            str(self.operator) + " " + \
            str(self.action) + " @" + \
            str(self.filename) + ":" + str(self.line)
            
        return rule

    def evaluate(self, http_transaction):
        variable = self.variable.evaluate(http_transaction)
        res = self.operator.evaluate(variable, http_transaction)
        return res

