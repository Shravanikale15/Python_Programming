import sys

def main():
    if(len(sys.argv)==2):
        directoryName=sys.argv[1]
        print("Directory Name:",directoryName)
    else:
        print("Invalid no fo arguments")


if __name__=="__main__":
    main()