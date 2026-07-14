import threading

def Thread1():
    for i in range(1, 51):
        print(i, end=" ")

def Thread2():
    for i in range(50, 0, -1):
        print(i, end=" ")

t1 = threading.Thread(target=Thread1)
t2 = threading.Thread(target=Thread2)

t1.start()
t1.join()      # Wait for Thread1 to finish

t2.start()
t2.join()