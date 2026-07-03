def palindrome(num):
    rem=0
    rev=0
    num1=num
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if(num1==rev):
        print("Palindrome")
    else:
        print("Not a Palindrome")

num = int(input("Enter Number: "))
palindrome(num)