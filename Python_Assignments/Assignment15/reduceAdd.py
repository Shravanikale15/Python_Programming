from functools import reduce
addition =lambda no1,no2:no1+no2

def main():
    data=[13,4,23,6,90,3]

    reduceData=reduce(addition,data)
    print("Addition of all is:",reduceData)

if __name__=="__main__":
    main()