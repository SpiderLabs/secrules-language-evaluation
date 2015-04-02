

from sec_core import *


class ModSec(SecCore):

    def __init__(self, rules, rules_file, verbose):
        SecCore.__init__(self, rules, rules_file, verbose)

    def __str__(self):
        return "ModSecurity instance."

