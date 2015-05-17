
import sys
import sec_parser
from sec_config import *
from sec_action import *
from sec_operator import *
from sec_variable import *
from sec_log import *


class SecCore():
    phase_names = ['REQUEST_HEADERS', 'REQUEST_BODY', 'RESPONSE_HEADERS', 'RESPONSE_BODY', 'LOGGING']

    def __init__(self, rules, rules_file, verbose = False):
        self.verbose = verbose

        self.SecRuleEngine = "DetectionOnly"
        self.SecRequestBodyAccess = "Off"
        self.SecRequestBodyLimit = 1310700
        self.SecRequestBodyNoFilesLimit = 131072
        self.SecRequestBodyInMemoryLimit = 131072
        self.SecRequestBodyLimitAction = "Reject"
        self.SecPcreMatchLimit = 1000
        self.SecPcreMatchLimitRecursion = 1000
        self.SecResponseBodyAccess = "Off"
        self.SecResponseBodyMimeType = "text/plain text/html text/xml"
        self.SecResponseBodyLimit = 524288
        self.SecResponseBodyLimitAction = "ProcessPartial"
        self.SecTmpDir = "/tmp/"
        self.SecDataDir = "/tmp/"
        self.SecUploadDir = "/tmp/"
        self.SecUploadKeepFile = "RelevantOnly"
        self.SecUploadFileMode = 0600
        self.SecDebugLog = "/tmp/"
        self.SecDebugLogLevel = 9
        self.SecAuditEngine = "RelevantOnly"
        self.SecAuditLogRelevantStatus = "^(?:5|4(?!04))"
        self.SecAuditLogParts = "ABIJDEFHZ"
        self.SecAuditLogType = "Serial"
        self.SecAuditLog = "/tmp/"
        self.SecArgumentSeparator = "&"
        self.SecCookieFormat = 0
        self.SecStatusEngine = "On" 


        self.phases = [[], [], [], [], []]
        self.__parse(rules, rules_file)

    def __len__(self):
        return sum([len(i) for i in self.phases])


    def include(self, content, filename = None):
        cont = ""
        lineno = 0
        for l in content:

            lineno = lineno + 1
            # Skip commented or empty lines
            if len(l) <= 0:
                continue
            if l[0] == "#":
                continue
            # If there is a line continuation append the next line
            if l[-1:] == '\\':
                subl = l[:-1]
                # Remove any trailing spaces greater than one space
                trailingSpaces = len(subl) - len(subl.rstrip())
                if(trailingSpaces > 1):
                    trailingSpaces -= 1
                    subl = subl[:-trailingSpaces]     
                # always strip leading spaces to remove tabs
                cont = cont + (subl).lstrip()
                # make sure that there is at most one trailing space
                continue
            
            # If we got here we're at the last line of a continuation
            # Or continuation is empty (non-continuated rule)
            if cont != "":
                # There should be no problem stripping whitespace here
                l = cont + l.strip()
                cont = ""

            if self.verbose:
                print "###" + str(l)

            sec_parser.lineno = lineno
            sec_parser.filename = filename

            # We have extracted the rule, give it to the parser
            print l
            rule = sec_parser.yacc.parse(l)

            if isinstance(rule, SecConfig):
                rule.evaluate(self)
            elif isinstance(rule, SecInclude):
                rule.evaluate(self)
            else:
                self.phases[rule.phase - 1].append(rule)

        
    def __parse(self, content, filename = None):
        return self.include(content, filename)


    def evaluate(self, http_transaction):
        i = 0

        skip = 0
        chained_skip = False

        j = 0
        for phase in self.phases:
            j = j + 1
            debug_log(4, "Starting phase " + SecCore.phase_names[j-1] + ".")
            debug_log(9, "This phase consists of " + str(len(phase)) + " rule(s).")
            for rule in phase:

                if skip > 0:
                    skip = skip - 1
                    print "skip action..."
                    next
                if chained_skip:
                    if not rule.chained:
                        chained_skip = False

                    print "chained skipeed."
                    next

                i = i + 1
                debug_log(4, "Recipe: Invoking rule " + str(rule.id) + "; " + \
                    "[file \"" + str(rule.filename) + "\"] " + \
                    "[line \"" + str(rule.line) + "\"] " + \
                    "[id \"" + str(rule.id) + "\"].")
                debug_log(5, "Rule " + str(rule.id) + ": " + str(rule.rule))
                ret = rule.evaluate(http_transaction)
                debug_log(4, "Rule returned " + str(ret) + ".")


                if not ret:
                    debug_log(9, "No match, not chained -> mode NEXT_RULE.")
                else:
                    debug_log(9, "Matched")
                    for a in rule.action:
                        if not a.pre_process:
                               print " ** ops, not sure what to do..."



