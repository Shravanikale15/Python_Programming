def chk(Num):
    if Num%5==0:
        return True
    else:
        return False


def main():
    num=int(input("Enter the Number:"))
    print(chk(num))

if __name__=="__main__":
    main()