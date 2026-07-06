from functools import reduce
maxNum =lambda no1,no2:no1 if no1>no2 else no2

def main():
    data=[13,4,23,6,90,3]

    reduceData=reduce(maxNum,data)
    print("Max number is:",reduceData)

if __name__=="__main__":
    main()