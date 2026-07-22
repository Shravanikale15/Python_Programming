def checkEven(value):
    if value%2==0:
        print("Its Even number..")
    else:
        print("Its Odd Number..")

def main():
    value=int(input("Enter Number:"))
    checkEven(value)


if __name__=="__main__":
    main()