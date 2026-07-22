checkEven=lambda no:(no%2==0)

Increment=lambda no:no+1
def main():
    Data=[13,12,8,10,11,20]
    print("Input Data is:",Data)
    
    FData=list(filter(checkEven,Data))
    print("Data after filter",FData)

    MData=list(map(Increment,FData))
    print("Data after map",MData)

if __name__=="__main__":
    main()