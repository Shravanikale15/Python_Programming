import Marvellous1 as mi

def main():
    print("Enter First Number")
    num1=int(input())

    print("Enter Second Number")
    num2=int(input())

    ret=mi.Addition(num1,num2)  

    print("Addition is:",ret)

if __name__=="__main__":
    main()
