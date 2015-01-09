#!/usr/bin/env python
import os
import sys

if len(sys.argv) != 2:
    print "Usage: ./createBmf.py pathname"
    sys.exit()

pathname =       sys.argv[1]

def createBmf():
    filenames =[]
    for(path,dirs,files) in os.walk(pathname):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if ext == ".ppm":
                filenames.append(filename)
            #print filename

    filenames.sort()
    bmfName = pathname + "//" + "file.bmf"
    try:
        #print bmfName
        fBmf = open(bmfName,"w")
    except IOError:
        print "Cannot Create bmf file"
        exit()
    fBmf.write(str(len(filenames)) + " 1\n")
    for filename in filenames:
        fBmf.write(filename)
        fBmf.write("\n")
    fBmf.close()

if __name__ == '__main__':
    createBmf()
