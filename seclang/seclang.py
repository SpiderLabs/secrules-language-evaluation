

from sec_core import *
from modsec import *


def core(rules, verbose = False):
    return SecCore(rules, verbose);


def modsec(rules, verbose = False):
    return ModSec(rules, verbose)

