def Addition(num1,num2):
    ans=0
    ans=num1+num2
    return ans

def main():
    print("Enter First Number")
    num1=int(input())

    print("Enter Second Number")
    num2=int(input())

    ret=Addition(num1,num2)

    print("Addition is:",ret)

if __name__=="__main__":
    main()
