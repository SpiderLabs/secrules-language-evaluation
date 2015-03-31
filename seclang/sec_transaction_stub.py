

class SecTransactionStub():

    def __init__(self):
        self.ARGS = {}
        self.cookies = {}
 
    def get_headers(self):
        raise "get_headers is not implemented."

    def get_header(self):
        raise "get_header is not implemented."
    
    def resolv_variable(self, variable):
        raise "resolv_variable is not implemented."

