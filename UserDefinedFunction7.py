def Calculations(no1,no2):
     mult=no1*no2
     Div=no1/no2

     return mult,Div
     
def main():
  value1=int(input("Enter First Number:"))
  value2=int(input("Enter second Number:"))
  ret1,ret2=Calculations(value1,value2)
  print("Multiplication is:",ret1)
  print("Division is:",ret2)

if __name__=="__main__":
     main()

     