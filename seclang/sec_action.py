
import inspect
import sys

class SecAction(object):

    def __init__(self, action):
        self.pre_process = False
        self.action = action

    def __str__(self):
        return "Action: " + str(self.action)

    def evaluate(self, core):
        print " *** Not implemented"

