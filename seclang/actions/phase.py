
from seclang.sec_action import SecActionMetadata
 
class phase(SecActionMetadata):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#phase
    """
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

