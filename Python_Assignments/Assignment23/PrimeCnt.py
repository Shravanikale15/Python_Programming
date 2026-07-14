from multiprocessing import Pool

def PrimeCount(n):
    count = 0

    for i in range(2, n + 1):
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            count += 1

    return count


def main():
    data = [10, 20, 30, 40]

    p = Pool()

    result = p.map(PrimeCount, data)

    print(result)

    p.close()
    p.join()
if __name__ == "__main__":
    main()