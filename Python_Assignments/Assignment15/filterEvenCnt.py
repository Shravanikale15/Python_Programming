evenNum=lambda num:(num if num%2==0 else None)


def main():
    data=[2,4,5,7,10,6]
    filterData=list(filter(evenNum,data))
    print(" Even numbers are:",len(filterData))
if __name__=="__main__":
    main()