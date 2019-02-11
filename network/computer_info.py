

# Python Program to Get IP Address
import getpass
import socket
import uuid
import sys
import psutil # this had to be installed by pip


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
MacAddr = uuid.getnode()
username = getpass.getuser()
PythonVer = sys.version
CPUPercent = psutil.cpu_percent()
MemVert = psutil.virtual_memory()
NetworkPackets = psutil.net_io_counters()

print("Your Computer Name is: " + hostname)
print("Current CPU percentage: " + str(CPUPercent))
print("Current Network Packets:" + str(NetworkPackets))
print("Current Virtual memory :" + str(MemVert))
print("Your Computer IP Address is: " + IPAddr)
print("Your Computer MAC address is:  " + str(MacAddr))
print("Your username is: " + username)
print("Python Version " + PythonVer)


