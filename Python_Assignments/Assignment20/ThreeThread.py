import threading

def Small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Small:", count)
    print("ID:", threading.get_ident())
    print("Name:", threading.current_thread().name)

def Capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Capital:", count)
    print("ID:", threading.get_ident())
    print("Name:", threading.current_thread().name)

def Digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Digits:", count)
    print("ID:", threading.get_ident())
    print("Name:", threading.current_thread().name)

str1 = input("Enter string: ")

t1 = threading.Thread(target=Small, args=(str1,), name="Small")
t2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
t3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()