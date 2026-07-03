def checkEven(value):
    if value%2==0:
        return True
    else:
        return False

def main():
    value=int(input("Enter Number:"))
    ret=checkEven(value)
    if(ret==True):
        print("Its Even Number..")
    else:
        print("Its Odd Number...")

if __name__=="__main__":
    main()