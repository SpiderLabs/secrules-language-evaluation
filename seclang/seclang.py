

from sec_core import *
from modsec import *


def core(rules, rules_file, verbose = False):
    return SecCore(rules, rules_file, verbose);


def modsec(rules, rules_file, verbose = False):
    return ModSec(rules, rules_file, verbose)

