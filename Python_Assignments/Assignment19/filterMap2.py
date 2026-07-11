from functools import reduce
n=int(input("Enter no of elements:"))
data=[]
for i in range(n):
    ele=int(input("Enter element:"))
    data.append(ele)

def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

increment=lambda  x: x * 2
add=lambda  x, y: x if x > y else y

def main():
    filterdata=list(filter(prime,data))
    print("Data after filter:",filterdata)
    mapdata=list(map(increment,filterdata))
    print("Data after map:",mapdata)
    reducedata=reduce(add,mapdata)
    print("Addition:",reducedata)

if __name__=="__main__":
    main()
