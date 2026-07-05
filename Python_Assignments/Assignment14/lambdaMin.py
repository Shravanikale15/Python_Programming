num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
minnum=lambda num1,num2: (num1<num2)
if minnum(num1,num2)==True:
    print("min number is:",num1)
else:
    print("min number is:",num2)
