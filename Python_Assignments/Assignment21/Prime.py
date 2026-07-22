import threading

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def Prime(data):
    print("Prime Numbers:")
    for i in data:
        if isPrime(i):
            print(i, end=" ")
    print()

def NonPrime(data):
    print("Non Prime Numbers:")
    for i in data:
        if not isPrime(i):
            print(i, end=" ")
    print()

data = [2, 5, 8, 9, 11, 15, 17, 20]

t1 = threading.Thread(target=Prime, args=(data,))
t2 = threading.Thread(target=NonPrime, args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()