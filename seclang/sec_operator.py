
import urllib
import os
import re

from sec_utils import *

libinjection_support = True
ipaddress_support = True
geoip_support = True

try:
    from libinjection import *
except:
    libinjection_support = False

try:
    import ipaddress
except:
    ipaddress_support = False

try:
    import GeoIP
except:
    geoip_support = False


class SecOperator():
    def __init__(self, operator, config=None):
        self.operator = operator
        self.path = None

        if config != None:
            self.path = os.path.dirname(config)

        self.op = self.operator.split(" ")[0]
        self.arg = ' '.join(self.operator.split(" ")[1:])


    def __str__(self):
        return "Operator: " + str(self.operator)

    def evaluate(self, variable, http_transaction):
        op = self.op
        comp = self.arg

        try:
            n_variable = int(variable)
        except:
            n_variable = 0

        try:
            n_comp = int(comp)
        except:
            n_comp = 0



        if op == "@rx":
            try:
                m = re.search(comp, variable)
                if m == None:
                    return False
                else:
                    return True
            except:
                return False
        if op == "@eq":
            return int(n_variable) == int(n_comp)
        elif op == "@ge":
            return int(n_variable) >= int(n_comp)
        elif op == "@gt":
            return int(n_variable) > int(n_comp)
        elif op == "@le":
            return int(n_variable) <= int(n_comp)
        elif op == "@lt":
            return int(n_variable) < int(n_comp)
        elif op == "@pm":
            for c in str(comp).split("|"):
                for c2 in c.split(" "):
                  if str(c2) in str(variable):
                      return True
 
            return False
 
        elif op == "@detectXSS":
            if libinjection_support:
                client9 = libinjection.xss(str(variable))
                return client9 == 1
            return False
        elif op == "@detectSQLi":
            if libinjection_support:
                s = sqli_state()
                sqli_init(s, str(variable), libinjection.FLAG_QUOTE_NONE | libinjection.FLAG_SQL_ANSI)
                client9 = libinjection.is_sqli(s)
                return client9 == 1
            return False
        elif op == "@strmatch":
            for c in str(comp).split("|"):
                if str(c) in str(variable):
                    return True
            return False
        elif op == "@ipMatch":
            if ipaddress_support:
                try:
                    return ipaddress.ip_address(unicode(variable)) in ipaddress.ip_network(unicode(comp), strict=False)
                except:
                    return False
            return False
        elif op == "@verifyCC":
            m = re.search(comp, variable)
            if m == None:
                return False
            variable = m.group(0)
            return luhn(str(variable))
        elif op == "@containsWord":
            if str(comp) == "":
                return True

            if str(comp) == str(variable):
                return True

            for b in [" ", ">", "<", '\x00']:
                if str(comp + b) in str(variable):
                    return True

                if str(b + comp) in str(variable):
                    return True

            return False
        elif op == "@beginsWith":
            return str(variable).startswith(str(comp))
        elif op == "@endsWith":
            return str(variable).endswith(str(comp))
        elif op == "@unconditionalMatch":
            if str(comp) == "":
                return True
            if str(variable) == "":
                return True

            return False
        elif op == "@noMatch":
            if str(comp) == "":
                return False
            if str(variable) == "":
                return False

            if str(comp) in str(variable):
                return False

            return True
        elif op == "@within":
            if str(variable) == "":
                return True

            if str(comp) == "":
                return False

            if str(variable) in str(comp):
                return True

            return False
        elif op == "@streq":
            return str(comp) == str(variable)
 
        elif op == "@pmFromFile":
            matches = []
            files = str(comp).split(" ")
            for fn in files:
                lines = [line.rstrip('\n') for line in open(os.path.join(self.path, fn))]
                matches = matches + lines
            
            for t in matches:
                if str(t) in str(variable):
                    return True

            return False
        elif op == "@validateByteRange":
            num = []

            for i in str(comp).split(","):

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

            for c in map(ord, variable):
                if not c in num:
                    return True

            return False
        elif op == "@contains":
            if str(comp) == "":
                return True

            if str(comp) in str(variable):
                return True


            return False

        elif op == "@validateUtf8Encoding":
            if variable == "":
                return False

            try:
            #print "****** A: " + str(v)
                a = variable.encode('raw-unicode-escape').decode('ISO-8859-1')
                a = variable.encode('raw-unicode-escape').decode('utf-8')
            except:
                return True

            return False

        elif op == "@validateUrlEncoding":
            if str(variable) == "":
                return False
            i = 0
            while i < len(str(variable)):
                if variable[i] == '%':
                    if i + 2 >= len(str(variable)):
                        return True
                    else:
                        c1 = variable[i+1]
                        c2 = variable[i+2]

                        if ((c1 >= '0' and c1 <= '9') or (c1 >= 'a' and c1 <= 'f') or (c1 >= 'A' and c1 <= 'F')) and ((c2 >= '0' and c2 <= '9') or (c2 >= 'a' and c2 <= 'f') or (c2 >= 'A' and c2 <= 'F')):
                            i = i + 2
                        else:
                            return True

                i = i + 1

            return False
        elif op == "@geoLookup":
            if str(variable) == "":
                return False

            # FIXME: Need to open the GeoIP.dat from the correct directory.
            if geoip_support:
                gi = GeoIP.open("GeoIP.dat", GeoIP.GEOIP_STANDARD)
                z = gi.record_by_addr(str(variable))

                return not z == None

            return False

        print " *** WARNING: I don't know anything about this operator: " + str(op)

        return False

