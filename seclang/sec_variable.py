

class SecVariable():
    def __init__(self, variable, transaction = None):
        self.name = variable
        self.transaction = transaction

    def __str__(self):
        return str(self.name)

    def content(self):
        return self.transaction.resolv_variable(self.name)

    def setTransaction(self, transaction):
        self.transaction = transaction

