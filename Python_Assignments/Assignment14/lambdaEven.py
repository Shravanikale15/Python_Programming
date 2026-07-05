num=int(input("Enter the number:"))
evennum=lambda num: (num%2==0)
if evennum(num)==True:
    print(True)
else:
    print(False)
