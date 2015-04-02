#!/usr/bin/env python

import sys, getopt
import os
from seclang import seclang
from http import dummy_http_parser as sec_transaction

def print_help():
    print "Use: " + str(sys.argv[0]) + " -r rules_file -d http_dump_file"


def print_head():
    print "ModSecurity seclang evaluation"
    print "This is a PoC. Not to use in production. It may let you down."
    print " "
    print "Report bugs on GitHub:"
    print "https://github.com/SpiderLabs/secrules-language-evaluation/issues/"
    print " "


def main(argv):
    secCore = None
    secTransactions = None
    verbose = False
    rules = None
    rules_file = None
    http_dump = None

    print_head()

    try:
        opts, args = getopt.getopt(argv[1:],"vhr:d:", ["rules=","dump="])
    except getopt.GetoptError:
        print_help();
        sys.exit(2)
    if len(opts) < 1:
        print_help();
        sys.exit(2)


    for opt, arg in opts:
        if opt == "-h":
            print_help();
            sys.exit()
        elif opt in ("-r", "--rules"):
            rules_file = os.path.abspath(arg)
        elif opt in ("-d", "--dump"):
            http_dump = arg
        elif opt == "-v":
            verbose = True
 
    if rules_file == None or http_dump == None:
        print_help();
        sys.exit()

    try:
        with open(rules_file) as f:
            rules = f.read().splitlines()
    except:
        print "Failed to open rules file: " + str(rules)
        sys.exit(2)

    secCore = seclang.modsec(rules, rules_file, verbose)

    if verbose:
        print "Loaded " + str(len(secCore)) + " rules."

    with open(arg) as f:
        http_dump = f.read()
    secTransactions = sec_transaction.parse(http_dump)

    for t in secTransactions:
        secCore.evaluate(t)

if __name__ == "__main__":
    main(sys.argv)

