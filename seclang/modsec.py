

from sec_core import *


class ModSec(SecCore):

    def __init__(self, rules, verbose):
        SecCore.__init__(self, rules, verbose)

    def __str__(self):
        return "ModSecurity instance."

