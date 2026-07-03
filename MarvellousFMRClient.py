from Marvellous_Library import filterX,mapX,reduceX
checkEven=lambda no:(no%2==0)

Increment= lambda no:no+1

Addition=lambda no1,no2:no1+no2

def main():
    Data=[13,12,8,10,11,20]
    print("Input Data is:",Data)
    
    FData=list(filterX(checkEven,Data))
    print("Data after filter",FData)

    MData=list(mapX(Increment,FData))
    print("Data after map",MData)

    RData=reduceX(Addition,MData)
    print("Data after reduce",RData)


if __name__=="__main__":
    main()