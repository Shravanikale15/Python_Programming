sqNum=lambda num:(num if num%2==0 else None)


def main():
    data=[2,4,5,7,10,6]
    filterData=list(filter(sqNum,data))
    print(" Even numbers are:",filterData)
if __name__=="__main__":
    main()