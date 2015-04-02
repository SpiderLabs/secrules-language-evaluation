#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
import json
from os import listdir, walk
from os.path import isfile, join
from seclang.sec_parser import sec_operator

from seclang.sec_operator import *

def print_help():
    print "Use: ",
    print str(sys.argv[0]),
    print " -p /path/to/unit/tests [-v] [-h]"


def play_test(filename):
    print "Starting test: " + str(filename)
    content = None
    with open(filename, "r") as f:
        content = f.read()
    content = json.loads(content)
    i = 0
    for t in content:
        i = i + 1
        if not 'param' in t:
            t['param'] = ""

        op = sec_operator(t['name'] + " " + t['param'], filename)
        ret = op.evaluate(t['input'], None)

        if int(t['ret']) == 0:
            test_ret = False
        elif int(t['ret']) == 1:
            test_ret = True

        if test_ret != ret:
            print "test failed:"
            print " - expected: " + str(test_ret)
            print " - received: " + str(ret)
            print " -     file: " + str(filename) + " number: " + str(i)
            print " -     test: " + str(t)
            print " - operator: " + str(op.__class__)


def main(argv):
    path = None
    try:
        opts, args = getopt.getopt(argv[1:],"vhp:", ["path="])
    except getopt.GetoptError:
        print_help();
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print_help();
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg

    if path == None:
        print_help()
        sys.exit(2)

    fs = []
    for (dirpath, dirnames, filenames) in walk(path):
        for f in filenames:
            f = dirpath + "/" + f
            fs.append(f)

    fs = [f for f in fs if f.endswith(".json")]

    for f in fs:
        play_test(f)


if __name__ == "__main__":
    main(sys.argv)

