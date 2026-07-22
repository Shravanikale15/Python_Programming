import sys

def main():
    if(len(sys.argv)==2):

        if(sys.argv[1]=="--H" or sys.argv[1]=="--h" ):
            print("Help")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage")
        else:
            directoryName=sys.argv[1]
            print("Directory Name:",directoryName)
    else:
        print("Invalid no fo arguments")
        print("Please use --h or --u for more information")

if __name__=="__main__":
    main()