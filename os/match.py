# the following code searches  for  text files on  your computer

import fnmatch
# Test whether the filename string matches the pattern string, returning True or False

import os


rootPath = '/'

pattern = '*.txt'

for root,dirs,files in os.walk(rootPath):
# The method walk() generates the file names in a directory tree
# by walking the tree either top-down or bottom-up

    for filename in fnmatch.filter(files,pattern):
        print(os.path.join(root,filename))
