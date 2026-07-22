import sys
import os
import hashlib

def calculateChecksum(FileName):
    #rb= read mode binary
    fobj=open(FileName,"rb")
    hobj=hashlib.md5() #md5 class object
    Buffer=fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)
    
    fobj.close()

    return hobj.hexdigest()

def main():
    ret=calculateChecksum("DemoX.txt")
  
    print("Checksum of file is:",ret)
if __name__=="__main__":
    main()