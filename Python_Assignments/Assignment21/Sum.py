import threading

def Sum(data):
    s = 0
    for i in data:
        s = s + i
    print("Sum =", s)

def Product(data):
    p = 1
    for i in data:
        p = p * i
    print("Product =", p)

data = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    data.append(num)

t1 = threading.Thread(target=Sum, args=(data,))
t2 = threading.Thread(target=Product, args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()