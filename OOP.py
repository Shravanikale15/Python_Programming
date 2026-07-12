class Arithmetic:
    def addtion(no1,no2):
        ans= no1+no2
        return ans

    def subtraction(no1,no2):
        ans= no1-no2
        return ans
    
aobj=Arithmetic()
no1=int(input("Enter First Number:"))
no2=int(input("Enter Second Number:"))

#ans=Addition(aobj,no1,no2)  TypeError 
ans=aobj.addtion(no1,no2)       #Error
print("Addition is :",ans)

ans=aobj.subtraction(no1,no2)   #Error
print("Subtraction is :",ans)