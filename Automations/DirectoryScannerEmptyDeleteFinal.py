
##################################################
#
# Importing Required Libraries
# 
#  
##################################################
import sys
import os
import time
import schedule
 ##################################################
    #
    # Funtion Name:       main
    # Input:              command line arguments
    # Description         it controls the script
    # Author              Shravani Kale
###################################################
def DirectoryScanner(DirectoryPath):
    
    Border="-"*40

    timestamp=time.ctime()
    #%s for string
    LogFileName="Marvellous%s.log"%(timestamp)

    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")
    ret=False
    ret=os.path.exists(DirectoryPath)

    if ret==False:
        print("Marvellous Automation Error: There is no such directory with name",DirectoryPath)
        return
    ret=os.path.isdir(DirectoryPath)

    if ret==False:
        print("Marvellous Automation Error: It is not directory with name",DirectoryPath)
        return
    
    print("Log File gets created with:",LogFileName)

    fobj=open(LogFileName,"w")
    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")
    fobj.write("Files from the directory are: \n")
    fobj.write(Border+"\n\n")
    TotalFiles=0
    EmptyFiles=0
    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles=TotalFiles+1
            fname=os.path.join(FolderName,fname)
            fobj.write(fname+"\n")
            print("File name ",fname," size:", {os.path.getsize(fname)})
            if(os.path.getsize(fname)==0):
                EmptyFiles=EmptyFiles+1
                os.remove(fname)
                
    fobj.write(Border+"\n")
    fobj.write("Total files Scanned:",TotalFiles)
    fobj.write("Total Empty files delete",EmptyFiles)

   
    fobj.write(Border+"\n")
    fobj.write("Log file gets created at:"+timestamp)
    fobj.write("\n"+Border+"\n")
    fobj.close()

def main():
    ##################################################
    #
    # Starter
    #
    #
    ##################################################
    Border="-"*40
    print(Border)
    print(" Marvellous Automation Script")
    print(Border)
    if(len(sys.argv)==2):

        if(sys.argv[1]=="--H" or sys.argv[1]=="--h" ):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Execute the script as ")
            print("Python Filename.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while(True):
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid no fo arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script")
    print(Border)

if __name__=="__main__":
    main()


