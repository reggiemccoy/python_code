
# Python Program to Get IP Address
import getpass
import socket
import uuid
import sys
import psutil # this had to be installed by pip
import shutil
import time
import schedule # this had to be installed by pip
import os

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
MacAddr = uuid.getnode()
username = getpass.getuser()
PythonVer = sys.version
CPUPercent = psutil.cpu_percent()
MemVert = psutil.virtual_memory()
NetworkPackets = psutil.net_io_counters()
DiskUsage_info = shutil.disk_usage
LaptopBattery = psutil.sensors_battery()



def comp_info():  # Created a function for  all the computer information

    print("Your Computer Name is: " + hostname)

    print("Current CPU percentage: " + str(CPUPercent))

    print("Current battery life if this system is a laptop: " + str(LaptopBattery))



    print("Your disk usage is: " + str(DiskUsage_info))

    print("Current Network Packets:" + str(NetworkPackets))

    print("Current Virtual memory :" + str(MemVert))

    print("Your Computer IP Address is: " + IPAddr)

    print("Your Computer MAC address is:  " + str(MacAddr))

    print("Your username is: " + username)

    print("Python Version " + PythonVer)

    print("\n") # Added the following to add spaces between the  output refresh

schedule.every(5).seconds.do(comp_info) # Created a schedule using a loop


while 1:


    schedule.run_pending()
    time.sleep(1)


