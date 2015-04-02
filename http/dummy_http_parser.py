
import Cookie
import re
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
from seclang.sec_transaction_stub import SecTransactionStub
from urlparse import parse_qs


def parse(content):
    # Not working with multiple requests yet.
    return [SecTransaction(content)]


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


class SecTransaction(SecTransactionStub, HTTPRequest):
    def __init__(self, plain):
        HTTPRequest.__init__(self, plain)
        SecTransactionStub.__init__(self)
        self.plain = plain

        args = {}
        try:
            url = ' '.join(self.path.split("?")[1:])
            args = parse_qs(url)
        except:
            pass

        # FIXME: this is not what we want to do.
        for k in args:
            v = args[k]
            self.ARGS[k] = v[0]


    def resolv_variable(self, variable):
        # TODO: Missing a lot of variables here.

        r = re.compile('([A-z0-9-_]+):([A-z0-9-_]+)')
        key_collection = r.findall(variable)

        value = None

        if variable.startswith("ARGS"):
            value = self.ARGS
        elif variable.startswith("ARGS_NAMES"):
            value = self.ARGS.keys()
        elif variable.startswith("QUERY_STRING"):
            value = self.path
        elif variable.startswith("REMOTE_ADDR"):
            #value = self.client_address[0]
            value = "127.0.0.1"
        elif variable.startswith("REQUEST_BASENAME"):
            value = self.headers['host']
        elif variable.startswith("REQUEST_BODY"):
            value = self.rfile
        elif variable.startswith("REQUEST_COOKIES"):
            #value = self.headers.get_all('Cookie',failobj=[])
            value = self.cookies
        elif variable.startswith("REQUEST_COOKIES_NAMES"):
            value = self.cookies.keys()
            #value = self.headers.get_all('Cookie',failobj=[]).keys()
        elif variable.startswith("REQUEST_FILENAME"):
            value = self.path
        elif variable.startswith("REQUEST_HEADERS"):
            value = {}
            for i in self.headers.keys():
                value[i] = self.headers.get(i)
        elif variable.startswith("REQUEST_HEADERS_NAMES"):
            value = self.headers.keys()
        elif variable.startswith("REQUEST_METHOD"):
            value = self.command
        elif variable.startswith("REQUEST_PROTOCOL"):
            value = self.request_version
        elif variable.startswith("REQUEST_URI"):
            value = self.path
        elif variable.startswith("RESPONSE_BODY"):
            value = None
        elif variable.startswith("RESPONSE_CONTENT_LENGTH"):
            value = None
        elif variable.startswith("RESPONSE_CONTENT_TYPE"):
            value = None
        elif variable.startswith("RESPONSE_HEADERS"):
            value = None
        elif variable.startswith("RESPONSE_HEADERS_NAMES"):
            value = None
        elif variable.startswith("RESPONSE_PROTOCOL"):
            value = None
        elif variable.startswith("RESPONSE_STATUS"):
            value = None

        try:
            if key_collection:
                value = value[key_collection[0][1].lower()]
        except:
            value = None

        return value


