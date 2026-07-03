from functools import reduce

checkEven=lambda no:(no%2==0)

def Increment(no):
    return no+1

def Addition(no1,no2):
    return no1+no2

def main():
    Data=[13,12,8,10,11,20]
    print("Input Data is:",Data)
    
    FData=list(filter(checkEven,Data))
    print("Data after filter",FData)

    MData=list(map(Increment,FData))
    print("Data after map",MData)

    RData=reduce(Addition,MData)
    print("Data after reduce",RData)

if __name__=="__main__":
    main()