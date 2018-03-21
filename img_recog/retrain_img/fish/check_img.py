import sys
import imghdr
from os import walk
import os

mypath = sys.argv[1]

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)    
    break

for fi in f:
    type_fi = imghdr.what(mypath+"/"+fi)
    if not type_fi in ["jpg","jpeg","png","gif"]:
        print(mypath+"/"+fi)
        os.remove(mypath+"/"+fi)



