from functools import reduce
minNum =lambda no1,no2:no2 if no1>no2 else no1

def main():
    data=[13,4,23,6,90,3]

    reduceData=reduce(minNum,data)
    print("Min number is:",reduceData)

if __name__=="__main__":
    main()