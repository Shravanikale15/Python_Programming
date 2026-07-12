class Arithmetic:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
        
    def addtion(self,no1,no2):
        ans= self.no1+self.no2
        return ans

    def subtraction(self,no1,no2):
        ans= self.no1-self.no2
        return ans
    
no1=int(input("Enter First Number:"))
no2=int(input("Enter Second Number:"))
aobj=Arithmetic(no1,no2)

#addition(aobj,no1,no2)
ans=aobj.addtion(no1,no2)      
print("Addition is :",ans)

#subtraction(aobj,no1,no2)
ans=aobj.subtraction(no1,no2)   
print("Subtraction is :",ans)