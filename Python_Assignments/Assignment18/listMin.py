n=int(input("Enter no. of elements:"))
data=[]
for i in range(n):
    ele=int(input("Enter element:"))
    data.append(ele)

min=0
for i in data:
    if(min>i):
        min=i

print("Min element:",min)
