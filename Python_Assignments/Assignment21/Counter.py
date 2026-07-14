import threading

counter = 0
lock = threading.Lock()

def Count():
    global counter

    for i in range(1000):
        lock.acquire()
        counter += 1
        lock.release()

t1 = threading.Thread(target=Count)
t2 = threading.Thread(target=Count)
t3=threading.Thread(target=Count)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter =", counter)