# The following creates a file inside of the folder directory of were this has been created.
"""""
    "x" - Create - will create a file, returns an error if the file exist

    "a" - Append - will create a file if the specified file does not exist

    "w" - Write - will create a file if the specified file does not exist
"""""
f = open("myfile.txt", "x")