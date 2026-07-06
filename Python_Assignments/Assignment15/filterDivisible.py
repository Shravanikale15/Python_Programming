divisibleNum=lambda num:(num if num%3==0 and num%5==0 else None)


def main():
    data=[1,4,15,7,30,6,45,60]
    filterData=list(filter(divisibleNum,data))
    print(" numbers divisible by 3 and 5:",filterData)
if __name__=="__main__":
    main()