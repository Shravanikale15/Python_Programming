num=int(input("Enter Number:"))
rem=0
cnt=0
while(num>0):
    rem=rem%10
    cnt=cnt+1
    num=num//10
print("no of digits is:",cnt)