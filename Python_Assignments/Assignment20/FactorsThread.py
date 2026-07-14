import threading

def EvenFactor(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum += i
    print("\nSum of Even Factors:", sum)

def OddFactor(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum += i
    print("\nSum of Odd Factors:", sum)

num = int(input("Enter number: "))

t1 = threading.Thread(target=EvenFactor, args=(num,))
t2 = threading.Thread(target=OddFactor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")