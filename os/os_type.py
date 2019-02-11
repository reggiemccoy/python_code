import os  # displays the OS information
import platform


print("OS type " + os.name)
# print(platform.release())
print(platform.system() +" " + platform.release())
print( "Build number: " + platform.version())