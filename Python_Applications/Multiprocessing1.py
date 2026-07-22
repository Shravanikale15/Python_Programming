import time
import multiprocessing
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

    tboj1=multiprocessing.Process(target=sumEven,args=(100000000,))
    tboj2=multiprocessing.Process(target=sumodd,args=(100000000,))
    tboj1.start()
    tboj2.start()
    tboj1.join()
    tboj2.join()
    end_time=time.perf_counter()
    print(f"Time requires is: {end_time-start_time:4f}")

if __name__=="__main__":
    main()