from functools import reduce
product =lambda no1,no2:no1*no2

def main():
    data=[4,6,3,1,10]

    reduceData=reduce(product,data)
    print("product of all is:",reduceData)

if __name__=="__main__":
    main()