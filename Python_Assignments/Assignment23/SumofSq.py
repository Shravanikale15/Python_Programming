from multiprocessing import Pool

def SumSquare(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i * i
    return sum

def main():
    data = [10, 20, 30, 40]

    p = Pool()

    result = p.map(SumSquare, data)

    print(result)

    p.close()
    p.join()
if __name__ == "__main__":
    main()