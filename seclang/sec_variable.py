

class SecVariable():
    def __init__(self, variable):
        self.name = variable

    def __str__(self):
        return "Variable: " + str(self.name)

    def evaluate(self, http_transaction):
        return http_transaction.resolv_variable(self.name)

