from Marvellous1 import Addition

def main():
    print("Enter First Number")
    num1=int(input())

    print("Enter Second Number")
    num2=int(input())

    ret=Addition(num1,num2)  

    print("Addition is:",ret)

    ret=Subtraction(num1,num2)  #Error

    print("Subtraction is:",ret)

if __name__=="__main__":
    main()
