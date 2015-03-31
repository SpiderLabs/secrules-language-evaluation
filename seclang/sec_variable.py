

class SecVariable():
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return "Variable: " + str(self.variable)

    def evaluate(self, http_transaction):
        return http_transaction.resolv_variable(self.variable)

