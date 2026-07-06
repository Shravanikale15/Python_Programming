sqNum=lambda num:num*num


def main():
    data=[2,4,5,7]
    mapData=list(map(sqNum,data))
    print("Square of numbers are:",mapData)
if __name__=="__main__":
    main()