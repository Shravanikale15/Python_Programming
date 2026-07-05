import time
def factorial(No):
    fact=1
    for i in range(1,No+1):
        fact=fact*i
    
    return fact

def main():
   value=int(input("Enter the number:"))
   start_time=time.time()
   ret=factorial(value)
   print(f"Factorial of {value} is {ret}")
   end_time=time.time()
   print("Time required is:", end_time-start_time)
   
if __name__=="__main__":
    main()