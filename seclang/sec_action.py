
import inspect
import sys


class SecAction(object):

    def __init__(self, action):
        if action.startswith("t:"):
            self.name = action[2:]
        else:
            self.name = action.split(":")[0]

        self.action = action

        self.pre_process = False
        self.is_transformation = False
        self.is_metadata = False

    def __str__(self):
        return "Action: " + str(self.name)

    def evaluate(self, core):
        print " *** Not implemented"

class SecActionTransformation(SecAction):

    def __init__(self, action):
        SecAction.__init__(self, action)
        self.is_transformation = True


class SecActionMetadata(SecAction):

    def __init__(self, action):
        SecAction.__init__(self, action)
        self.is_metadata = True
        self.pre_process = True


