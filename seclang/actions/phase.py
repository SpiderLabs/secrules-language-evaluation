
from seclang.sec_action import SecAction
 
class phase(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#phase
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        phase = self.action[6:]
        if phase == "request":
            phase = 2
        elif phase == "response":
            phase = 4
        elif phase == "logging":
            phase = 5

        phase = int(phase)

        core.phase = phase
        return phase

