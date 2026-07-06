def chk(Num):
    if Num>0:
        print("Positve")
    elif Num==0:
        print("Zero")
    else:
        print("Negative")


def main():
    num=int(input("Enter the Number:"))
    chk(num)

if __name__=="__main__":
    main()