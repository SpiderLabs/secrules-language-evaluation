#!/usr/bin/python

import sys
from ply import lex as lex
from ply import yacc as yacc

from sec_core import *
from sec_config import *
from sec_variable import *
from sec_operator import *
from sec_action import *
from sec_rule import *

import inspect
from actions import *
from operators import *

filename = None
lineno = None

tokens = (
        "DIRECTIVE",
        "VARIABLE",
        "OPERATOR",
        "ACTION",
        "TRANSFORMATION",
        "SPACE",
        "QUOTAION_MARK",
        "COMMA",
        "CONFIG_DIRECTIVE",
        "FREE_TEXT",
        "CONFIG_INCLUDE",
        "CONTROL"
        )

def t_CONFIG_INCLUDE(t):
    r"Include"
    return t

def t_CONFIG_DIRECTIVE(t):
    r"SecRuleEngine|SecRequestBodyAccess|SecResponseBodyAccess|SecRequestBodyLimitAction|SecRequestBodyNoFilesLimit|SecRequestBodyInMemoryLimit|SecRequestBodyLimit|SecPcreMatchLimitRecursion|SecPcreMatchLimit|SecResponseBodyMimeType|SecResponseBodyLimitAction|SecResponseBodyLimit|SecTmpDir|SecDataDir|SecDebugLogLevel|SecDebugLog|SecAuditEngine|SecAuditLogRelevantStatus|SecAuditLogParts|SecAuditLogType|SecAuditLog|SecArgumentSeparator|SecCookieFormat|SecStatusEngine"
    return t

def t_DIRECTIVE(t):
    r"(?i)SecRule"
    return t

def t_VARIABLE(t):
    r"(?i)((\|){0,1}((ARGS_NAMES|ARGS|QUERY_STRING|REMOTE_ADDR|REQUEST_BASENAME|REQUEST_BODY|REQUEST_COOKIES_NAMES|REQUEST_COOKIES|REQUEST_FILENAME|REQUEST_HEADERS_NAMES|REQUEST_HEADERS|REQUEST_METHOD|REQUEST_PROTOCOL|REQUEST_URI|RESPONSE_BODY|RESPONSE_CONTENT_LENGTH|RESPONSE_CONTENT_TYPE|RESPONSE_HEADERS_NAMES|RESPONSE_HEADERS|RESPONSE_PROTOCOL|RESPONSE_STATUS|TX)(:([^ \|\"]+)){0,1}|REQBODY_ERROR|MULTIPART_STRICT_ERROR|MULTIPART_UNMATCHED_BOUNDARY|REMOTE_ADDR|REQUEST_LINE))+"
    return t

def t_OPERATOR(t):
    r"!?(@contains|@rx|@eq|@pm) ((?:(?!\")[^\\]|(?:\\\\)*\\[^\\])*)"
    return t

def t_CONTROL(t):
    r"ctl:[A-z0-9-_=+]+"
    return t

def t_ACTION(t):
    r"(allow|id:([0-9]+)|id:'([0-9]+)'|rev:'([0-9]+)'|rev:([0-9]+)|severity:([0-9])|severity:'([0-9])'|deny|block|skip|chain|phase:([0-6])|pass|nolog|status:([0-9]+)|capture)|((msg|logdata|data|setvar|tag):'((?:(?!\')[^\\]|(?:\\\\)*\\[^\\])*)')|(log|setvar:[^,]+)"
    return t

def t_TRANSFORMATION(t):
    r"t:(lowercase|urlDecodeUni|urlDecode|none|compressWhitespace|removeWhitespace|replaceNulls|removeNulls|htmlEntityDecode|jsDecode|cssDecode)"
    return t

def t_SPACE(t):
    r"\t|[ ]"
    return t

def t_QUOTAION_MARK(t):
    r"\""
    return t

def t_COMMA(t):
    r","
    return t

def t_FREE_TEXT(t):
    r"[^\"]+"
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()

def p_secrule(p):
    """
    secrule : spaces secrulet
    secrule : secrulet
    """
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]
        

def p_secrulet(p):
    """
    secrulet : CONFIG_INCLUDE spaces FREE_TEXT
    secrulet : CONFIG_DIRECTIVE spaces FREE_TEXT
    secrulet : CONFIG_DIRECTIVE spaces QUOTAION_MARK FREE_TEXT QUOTAION_MARK
    secrulet : DIRECTIVE spaces variable spaces QUOTAION_MARK operator QUOTAION_MARK spaces QUOTAION_MARK actions QUOTAION_MARK
    secrulet : DIRECTIVE spaces variable spaces QUOTAION_MARK operator QUOTAION_MARK
    secrulet : DIRECTIVE spaces variable spaces QUOTAION_MARK FREE_TEXT QUOTAION_MARK spaces QUOTAION_MARK actions QUOTAION_MARK
    secrulet : DIRECTIVE spaces variable spaces QUOTAION_MARK FREE_TEXT QUOTAION_MARK
    """
    if p[1] == "SecRule":
        if len(p) == 8:
            p[0] = SecRule(p[1], p[3], p[6], None, p.lexer.lexdata, lineno, filename)
        else:
            p[0] = SecRule(p[1], p[3], p[6], p[10], p.lexer.lexdata, lineno, filename)

    elif p[1] == "Include":
        p[0] = SecInclude(p[3], filename)
    else:
        if len(p) == 4:
            p[0] = SecConfig(p[1], p[3])
        else:
            p[0] = SecConfig(p[1], p[4])


def p_spaces(p):
    """
    spaces : SPACE
    spaces : SPACE spaces
    """


def p_variable(p):
    """
    variable : VARIABLE
    variable : QUOTAION_MARK VARIABLE QUOTAION_MARK
    """
    if len(p) == 2:
        p[0] = SecVariable(p[1])
    else:
        p[0] = SecVariable(p[2])


def p_split(p):
    """
    split : COMMA spaces
    split : spaces COMMA
    split : COMMA
    """
    p[0] = None


def p_actions(p):
    """ 
    actions : ACTION
    actions : CONTROL
    actions : ACTION split actions
    actions : TRANSFORMATION split actions
    actions : CONTROL split actions
    """
    if len(p) == 2:
        action = sec_action(p[1])
        p[0] = [action]
    else:
        action = sec_action(p[1])
        p[0] = [action] + p[3]


def sec_operator(operator, config):
    operator_class = None

    op = operator[0:].split(" ")[0].lower()
    # Remove the @ if it exists
    if(op[0] == '@'):
        op = op[1:]
    modules = inspect.getmembers(sys.modules["seclang.operators"], inspect.ismodule)
    for n, p in modules:
        if p.__package__ == "seclang.operators":
            if op == n:
                operator_class = getattr(p, n)(operator, config)

    if operator_class == None:
        raise BaseException("Operator not found: " + str(operator) + "/" + str(op))

    return operator_class

def sec_action(action):
    action_class = None

    if action[:2] == "t:":
        op = "transformation_" + str(action[2:])
    else:
        op = action.split(":")[0]

    modules = inspect.getmembers(sys.modules["seclang.actions"], inspect.ismodule)
    for n, p in modules:
        if p.__package__ == "seclang.actions":
            if op == n:
                action_class = getattr(p, n)(action)

    if action_class == None:
        raise BaseException("Action not found: " + str(action) + "/" + str(op))

    return action_class


def p_operator(p):
    """
    operator : OPERATOR
    """
    p[0] = sec_operator(p[1], config=filename)


def p_error(p):
    print "Problems parsing: "
    print " ** " + str(p.lexer.lexdata)
    print " "
    print "Tokens:"
    lex.input(p.lexer.lexdata)
    for tok in iter(lex.token, None):
        print repr(tok.type), repr(tok.value)
    sys.exit(2)

yacc.yacc()

