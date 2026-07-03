def digitCnt(num):
    rem=0
    cnt=0
    while(num!=0):
        rem=num%10
        cnt=cnt+1
        num=num//10
    print(cnt)

num = int(input("Enter Number: "))
digitCnt(num)