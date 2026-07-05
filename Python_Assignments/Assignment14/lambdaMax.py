num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
maxnum=lambda num1,num2: (num1>num2)
if maxnum(num1,num2)==True:
    print("max number is:",num1)
else:
    print("max number is:",num2)
