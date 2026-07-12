class Arithmetic:
    def addtion(self,no1,no2):
        ans= no1+no2
        return ans

    def subtraction(self,no1,no2):
        ans= no1-no2
        return ans
    
aobj=Arithmetic()
no1=int(input("Enter First Number:"))
no2=int(input("Enter Second Number:"))

 
ans=aobj.addtion(no1,no2)      
print("Addition is :",ans)

ans=aobj.subtraction(no1,no2)   
print("Subtraction is :",ans)