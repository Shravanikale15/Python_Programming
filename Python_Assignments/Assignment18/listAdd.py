n=int(input("Enter no. of elements:"))
data=[]
for i in range(n):
    ele=int(input("Enter element:"))
    data.append(ele)

sum=0
for i in data:
    sum=sum+i

print("Sum of elements:",sum)
