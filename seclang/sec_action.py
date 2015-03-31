

class SecAction(object):

    def __init__(self, action):
        self.pre_process = False
        self.action = action

    def __str__(self):
        return "Action: " + str(self.action)

    def evaluate(self, core):
        print " *** Not implemented"


class SecAction_Allow(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#allow
    """
    def evaluate(self, core):
        return True


class SecAction_Msg(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#msg
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        a = self.action[4:]
        if a[0] == "'":
            a = a[1:-1]
        core.msg = a
        return a


class SecAction_Id(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#id
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        id = self.action[3:]
        if id[0] == "'":
            id = id[1:-1]
        id = int(id)
        core.id = id
        return id


class SecAction_Rev(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#rev
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        a = self.action[4:]
        if a[0] == "'":
            a = a[1:-1]
        core.rev = a
        return a


class SecAction_Severity(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#severity
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        a = self.action[7:]
        if a[0] == "'":
            a = a[1:-1]
        
        if a == "EMERGENCY":
            a = 0
        elif a == "ALERT":
            a = 1
        elif a == "CRITICAL":
            a = 2
        elif a == "ERROR":
            a = 3
        elif a == "WARNING":
            a = 4
        elif a == "NOTICE":
            a = 5
        elif a == "INFO":
            a = 6
        elif a == "DEBUG":
            a = 7

        a = int(a)
        core.severity = a
        return a


class SecAction_Log(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#log
    """
    def evaluate(self, core):
        #print " ** LOG should goes to the apache error log and audit log"
        return True


class SecAction_Deny(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#deny
    """
    def evaluate(self, core):
        #print " ** Stops rule processing and intercept the transaction."
        return True


class SecAction_Block(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#block
    """
    def evaluate(self, core):
        #print " ** Performs what is defined at SecDefaultAction."
        return True


class SecAction_Status(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#status
    """
    def evaluate(self, core):
        #print " ** Specifies the response status code to use with actions deny and redirect."
        return 404


class SecAction_Skip(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#skip
    """
    def evaluate(self, core):
        skip = self.action[5:]
        if skip[0] == "'":
            skip = skip[1:-1]
        skip = int(skip)
        return skip


class SecAction_Chain(SecAction):
    """
    https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#chain
    """
    def __init__(self, action):
        SecAction.__init__(self, action)
        self.pre_process = True

    def evaluate(self, core):
        core.chained = True
 

class SecAction_Phase(SecAction):
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


