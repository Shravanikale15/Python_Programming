#Hybrid Application

checkEven=lambda no:(no%2==0)  

def main():
    value=int(input("Enter Number:"))
    ret=checkEven(value)  #Ret-value%2==0
    if(ret==True):
        print("Its Even Number..")
    else:
        print("Its Odd Number...")

if __name__=="__main__":
    main()