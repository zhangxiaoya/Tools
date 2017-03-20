
import os
import sys

if len(sys.argv) == 1:
    print("Usage: ./getFileNames PATHNAME FORMAT")
    print(" ")
    print("Note: ")
    print("----: PATHNAME must be input")
    print("----: Default forMat = lib")
    print(" ")
    sys.exit()
    
if len(sys.argv) == 2:
    forMat = ".lib"
else:
    forMat = "." + sys.argv[2]

pathname = sys.argv[1]

fileNameList = [];

def rename():
    for(path,dirs,files) in os.walk(pathname):
        idx = 0
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if(ext == forMat):
                fileNameList.append(filename)
                print(filename)

    saveReultFullName = pathname + "\\names.txt"
    saveFileNames = open(saveReultFullName,'w')
    saveFileNames.writelines([name + '\n' for name in fileNameList])
    saveFileNames.close()

if __name__ == '__main__':
    rename()
