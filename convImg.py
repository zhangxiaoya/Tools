#!/usr/bin/env python
import Image
import os
import sys

if len(sys.argv) != 4:
    print "Usage: ./convertImg.py pathname source_type target_type"
    sys.exit()

pathname =       sys.argv[1]
argOld   = "." + sys.argv[2]
argNew   = "." + sys.argv[3]

def converFormat():
    for(path,dirs,files) in os.walk(pathname):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            name = os.path.splitext(filename)[0]
            if(ext == argOld):
                newname = name + argNew
                newname = path + "//" + newname
                oldname = path + "//" + filename
                Image.open(oldname).save(newname)

if __name__ == '__main__':
    converFormat()
