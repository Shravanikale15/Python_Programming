def main():
    ans=0
    try:
        print("Enter First Number:")
        num1=int(input())
        print("Enter Second Number:")
        num2=int(input())
        ans=num1/num2
        print("Division is Successful")

    except ZeroDivisionError as zobj:
        print("Exception Occurred due to second operand is zero",zobj)

    print("Result is:",ans)


if __name__=="__main__":
    main()