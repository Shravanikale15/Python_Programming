n=int(input("Enter no. of elements:"))
data=[]
for i in range(n):
    ele=int(input("Enter element:"))
    data.append(ele)

max=0
for i in data:
    if(max<i):
        max=i

print("Max element:",max)
