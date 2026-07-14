import threading

def Maximum(data):
    print("Maximum =", max(data))

def Minimum(data):
    print("Minimum =", min(data))

data = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Maximum, args=(data,))
t2 = threading.Thread(target=Minimum, args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()