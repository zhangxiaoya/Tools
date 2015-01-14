#!/usr/bin/env python
import os
import sys

if len(sys.argv) == 1:
    print "Usage: ./renmDS pathname forMat"
    print "before rename:"
    print "--pathname"
    print "--+ oldfilename-1.fotMat"
    print "--+ oldfilename-2.fotMat"
    print "        ......         "
    print "--+ oldfilename-n.fotMat"
    print "after rename:"
    print "--pathname"
    print "--+        00001.format"
    print "--+        00002.format"
    print "        ......         "
    print "--+        0000n.format"
    print " "
    print "Note: Default forMat = ppm"
    print " "
    sys.exit()
if len(sys.argv) == 2:
    forMat = ".ppm"
else:
    forMat = "." + sys.argv[2]

pathname = sys.argv[1]

reguStr = '%05d'

def rename():
    for(path,dirs,files) in os.walk(pathname):
        idx = 0
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if(ext == forMat):
                #newname = filename.replace(" ","_")
                idx = idx + 1
                numIdx = reguStr%idx
                print numIdx
                newname = str(numIdx)
                newname = newname + forMat
                oldpath = path + "//" + filename
                newpath = path + "//" + newname
                try:
                    os.rename(oldpath,newpath)
                except BaseException, e:
                    print(str(e))
                print newpath

if __name__ == '__main__':
    rename()
