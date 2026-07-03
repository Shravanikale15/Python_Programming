def even(num):
    for i in range(1,num+1):
        if(i%2==0):
            print(i)
num=int(input("Enter Number:"))
even(num)