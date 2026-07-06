def chkEven(Num):
    if Num%2==0:
        print("Even Number")
    else:
        print("Odd Number")


def main():
    num=int(input("Enter the Number:"))
    chkEven(num)

if __name__=="__main__":
    main()