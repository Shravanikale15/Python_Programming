import threading

def EvenList(data):
    sum = 0
    print("Even Numbers:", end=" ")
    for i in data:
        if i % 2 == 0:
            print(i, end=" ")
            sum += i
    print("\nSum:", sum)

def OddList(data):
    sum = 0
    print("Odd Numbers:", end=" ")
    for i in data:
        if i % 2 != 0:
            print(i, end=" ")
            sum += i
    print("\nSum:", sum)

data = [1,2,3,4,5,6,7,8,9,10]

t1 = threading.Thread(target=EvenList, args=(data,))
t2 = threading.Thread(target=OddList, args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()