#!/usr/bin/env python
import os
def rename():
    path = raw_input("Please input the path name ")
    print path
    forMat = raw_input("Please input the extention ")
    print forMat
    for(path,dirs,files) in os.walk(path):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            name = os.path.splitext(filename)[0]
            if(ext == forMat):
                print filename
                print name
                name_part = name.replace("frame_","")
                newname = str(int(name_part)) + forMat
                oldpath = path + "//" + filename
                newpath = path + "//" + newname
                try:
                    os.rename(oldpath,newpath)
                except BaseException, e:
                    print(str(e))
                print newpath

if __name__ == '__main__':
    rename()
