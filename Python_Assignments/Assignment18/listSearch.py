n=int(input("Enter no. of elements:"))
data=[]
for i in range(n):
    ele=int(input("Enter element:"))
    data.append(ele)

num=int(input("Enter element to search"))
cnt=0

for i in data:
    if num==i:
        cnt=cnt+1

print("Frequency of element is:",cnt)