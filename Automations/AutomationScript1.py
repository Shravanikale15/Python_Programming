import sys

def main():
    directoryName=sys.argv[1]
    print("Name of Directory is:",directoryName)
    print(len(sys.argv))

if __name__=="__main__":
    main()