

# Python Program to Get IP Address
import getpass
import socket
import uuid
import sys
import subprocess


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
MacAddr = uuid.getnode()
username = getpass.getuser()
PythonVer = sys.version


print("Your Computer Name is: " + hostname)

print("Your Computer IP Address is: " + IPAddr)
print("Your Computer MAC address is:  " + str(MacAddr))
print("Your username is: " + username)
print("Python Version " + PythonVer)


