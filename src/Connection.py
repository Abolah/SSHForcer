from threading import Thread

class Connection(Thread):
    """
    This is the class that checks if a specific
    Username and password combination was successful.
    """

    def __init__(self, username, password, targetIp, portNumber, timeoutTime):

        super(Connection, self).__init__()

        self.username = username
        self.password = password
        self.targetIp = targetIp
        self.portNumber = portNumber
        self.timeoutTime = timeoutTime
        self.status = ""

    def run(self):

        sshConnection = SSHClient()
        sshConnection.set_missing_host_key_policy(AutoAddPolicy())

        try:
            sshConnection.connect(self.targetIp, port=int(self.portNumber),
                                  username=self.username, password=self.password,
                                  timeout=int(self.timeoutTime), allow_agent=False, look_for_keys=False)

            self.status = 'Succeeded'
            sshConnection.close()
        except:
            self.status = 'Failed'
