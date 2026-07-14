from multiprocessing import Pool
import time

def SumPower(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i ** 5

    return sum

def main():
    data = [10, 20, 30, 40]

    start = time.time()

    p = Pool()

    result = p.map(SumPower, data)

    print(result)

    p.close()
    p.join()

    end = time.time()

    print("Execution Time:", end - start)
if __name__ == "__main__":
    main()