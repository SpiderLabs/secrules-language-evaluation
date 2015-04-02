
import inspect
import sys


class SecAction(object):

    def __init__(self, action):
        self.name = action.split(":")[0]
        self.action = action

        self.pre_process = False
        self.is_transformation = False

    def __str__(self):
        return "Action: " + str(self.name)

    def evaluate(self, core):
        print " *** Not implemented"

class SecActionTransformation(SecAction):

    def __init__(self, action):
        SecAction.__init__(self, action)
        self.is_transformation = True


