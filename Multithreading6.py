import time
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
    start_time=time.perf_counter()
    
    sumEven(100000000000)
    sumodd(100000000000)
    end_time=time.perf_counter()
    print(f"Time requires is: {end_time-start_time:4f}")

if __name__=="__main__":
    main()