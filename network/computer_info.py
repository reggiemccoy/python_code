

# Python Program to Get IP Address
import getpass
import socket
import uuid


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
MacAddr = uuid.getnode()
username = getpass.getuser()


print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)
print("Your Computer MAC address is:  " + str(MacAddr))
print("Your username is: " + username)


