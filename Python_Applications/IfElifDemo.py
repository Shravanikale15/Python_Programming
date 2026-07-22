print("--------------------------------------")
print("---------Ticket Pricing Software------")
print("--------------------------------------")
print("Enter your Age:")

age=int(input())

if(age>0 and age<=5):
    print("Free Entry")
elif(age>5 and age<=18):
    print("Ticket Price is 900")
elif(age>18 and age<=40):
    print(" Ticket Price is 1200")
else:
    print("Ticket Price is 500")


