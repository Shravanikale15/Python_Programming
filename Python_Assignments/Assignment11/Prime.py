def prime(num):
    if num <= 1:
        print("Not a Prime Number")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            return

    print("Prime Number")

num = int(input("Enter Number: "))
prime(num)