#!/usr/bin/env python
import os
import sys

if len(sys.argv) == 1:
    print("Usage: ./rename-order pathname forMat")
    print("before rename:")
    print("--pathname")
    print("--+ oldfilename-0001_some-string.fotMat")
    print("--+ oldfilename-0002_some-string.fotMat")
    print("        ......         ")
    print("--+ oldfilename-000n_some-string.fotMat")
    print("after rename:")
    print("--pathname")
    print("--+        00001.format")
    print("--+        00002.format")
    print("        ......         ")
    print("--+        0000n.format")
    print(" ")
    print("Note: Default forMat = bmp")
    print(" ")
    sys.exit()
if len(sys.argv) == 2:
    forMat = ".bmp"
else:
    forMat = "." + sys.argv[2]

pathname = sys.argv[1]

reguStr = '%05d'

def rename():
    for(path,dirs,files) in os.walk(pathname):
        idx = 0
        for filename in files:
            fileName, extention = os.path.splitext(filename)
            if(extention == forMat):
                firstPart = fileName.split('-')
                newFileName = fileName + "-" + firstPart
                print(fileName + "  =>  " + newFileName)
                # newname = newname + forMat
                # oldpath = path + "//" + filename
                # newpath = path + "//" + newname
                # try:
                    # os.rename(oldpath,newpath)
                # except BaseException, e:
                    # print(str(e))
                # print newpath

if __name__ == '__main__':
    rename()
