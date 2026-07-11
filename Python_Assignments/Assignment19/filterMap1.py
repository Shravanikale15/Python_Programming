from functools import reduce
n=int(input("Enter no of elements:"))
data=[]
for i in range(n):
    ele=int(input("Enter element:"))
    data.append(ele)

greaterFilter=lambda num: num if num%2==0 else None

increment=lambda no:no*no

add=lambda num1,num2:num1+num2

def main():
    filterdata=list(filter(greaterFilter,data))
    print("Data after filter:",filterdata)
    mapdata=list(map(increment,filterdata))
    print("Data after map:",mapdata)
    reducedata=reduce(add,mapdata)
    print("Addition:",reducedata)

if __name__=="__main__":
    main()
