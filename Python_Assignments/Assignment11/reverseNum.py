def digitCnt(num):
    rem=0
    rev=0
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)

num = int(input("Enter Number: "))
digitCnt(num)