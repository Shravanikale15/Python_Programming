num=int(input("Enter the number:"))
oddnum=lambda num: (num%2==1)
if oddnum(num)==True:
    print(True)
else:
    print(False)
