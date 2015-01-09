#!/usr/bin/env python
import os
import sys

if len(sys.argv) != 3:
    print "Usage: ./renmDS pathname forMat"
    sys.exit()

pathname = sys.argv[1]
forMat = "." + sys.argv[2]
def rename():
    for(path,dirs,files) in os.walk(pathname):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if(ext == forMat):
                newname = filename.replace(" ","_")
                oldpath = path + "//" + filename
                newpath = path + "//" + newname
                try:
                    os.rename(oldpath,newpath)
                except BaseException, e:
                    print(str(e))
                print newpath

if __name__ == '__main__':
    rename()
