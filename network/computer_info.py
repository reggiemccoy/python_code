

# Python Program to Get IP Address
import getpass
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
username = getpass.getuser()
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
print(username)
