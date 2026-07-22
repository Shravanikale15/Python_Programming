import sys

def main():
    print("--------------------------------------------------------")
    print(" Marvellous Automation Script")
    print("--------------------------------------------------------")
    if(len(sys.argv)==2):

        if(sys.argv[1]=="--H" or sys.argv[1]=="--h" ):
            print("This automation script is used to travel the diorectpry")
            print("For better usage please check --u flag")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Execute the script as ")
            print("Python Filename.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            directoryName=sys.argv[1]
            print("Directory Name:",directoryName)
    else:
        print("Invalid no fo arguments")
        print("Please use --h or --u for more information")

    print("--------------------------------------------------------")
    print(" Thank you for using Marvellous Automation Script")
    print("--------------------------------------------------------")

if __name__=="__main__":
    main()