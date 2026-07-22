def sumEven(no):
    sum=0
    for i in range(2,no,2):
        sum=sum+i
    print("Sum of even:",sum)
def sumodd(no):
    sum=0
    for i in range(1,no,2):
        sum=sum+i
    print("Sum of odd",sum)
def main():
    sumEven(100000000)
    sumodd(100000000)

if __name__=="__main__":
    main()