#!/usr/bin/env python
import os
import sys

if len(sys.argv) != 3:
    print "Usage: ./renmDS pathname forMat"
    sys.exit()

pathname = sys.argv[1]
forMat = "." + sys.argv[2]

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
