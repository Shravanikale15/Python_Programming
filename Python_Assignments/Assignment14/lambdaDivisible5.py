num=int(input("Enter the number:"))
ret=lambda num: (num%5==0)
if ret(num)==True:
    print(True)
else:
    print(False)
