import os
import subprocess
import random


class Windscribe:
    def __init__(self, serverlist, user, password):
        """loads server list and logs into Windscribe"""
        with open(serverlist, 'r') as f:
            self.servers = f.read().splitlines()
        self.login(user,password)

    def login(self, user, password):
        """logs into Windscribe using provided credentials"""
        commands = ["windscribe-cli", "login"]
        proc = subprocess.Popen(commands, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.stdin.write(user)
        proc.stdin.write(password)

    def locations(self):
        """prints the locations available to connect to in the shell"""
        os.system("windscribe-cli locations")
        print(self.servers)

    def connect(self, server=None, rand=False):
        """connects to given server, best available server if no server given, or random server"""
        if rand:
            choice = random.choice(self.servers)
            os.system(f"windscribe-cli connect '{choice}'")
        elif server != None:
            os.system(f"windscribe-cli connect '{server}'")
        else:
            os.system("windscribe-cli connect 'Best'")
    
    def disconnect(self):
        """disconnect from the current server"""
        os.system("windscribe-cli disconnect")

    def logout(self):
        """logout of windscribe"""
        os.system("windscribe-cli logout")
