def odd(num):
    for i in range(1,num+1):
        if(i%2==1):
            print(i)
num=int(input("Enter Number:"))
odd(num)