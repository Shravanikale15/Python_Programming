from multiprocessing import Pool
import os

def Factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Process ID:", os.getpid())
    print("Input:", n)
    print("Factorial:", fact)
def main():
    data = [10, 15, 20, 25]

    p = Pool()

    p.map(Factorial, data)

    p.close()
    p.join()
if __name__ == "__main__":
    main()