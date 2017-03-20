
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
    FORMAT = ".lib"
else:
    FORMAT = "." + sys.argv[2]

PATHNAME = sys.argv[1]

debugFileNameList = []
releaseFileNameList = []

print("Start reading files")
print("Finding...")
def getFileName():
    for(path, dirs, files) in os.walk(PATHNAME):
        idx = 0
        for filename in files:
            name = os.path.splitext(filename)[0]
            ext = os.path.splitext(filename)[1]
            if(ext == FORMAT):
                if(name[-1] == 'd'):
                  debugFileNameList.append(filename)
                else:
                    releaseFileNameList.append(filename)
                print(filename)

    saveReultFullName = PATHNAME + "\\releaseNames.txt"
    saveFileNames = open(saveReultFullName, 'w')
    saveFileNames.writelines([name + '\n' for name in releaseFileNameList])
    saveFileNames.close()

    saveReultFullName = PATHNAME + "\\debugNames.txt"
    saveFileNames = open(saveReultFullName, 'w')
    saveFileNames.writelines([name + '\n' for name in debugFileNameList])
    saveFileNames.close()


if __name__ == '__main__':
    getFileName()
    print("Done!")
