
lenStr=lambda str:str if len(str)>5 else None
def main():
   stringlist=["c++","java","Python","Machine Learning","AI"]

   filterData=list(filter(lenStr,stringlist))
   print("Strings with length greater than 5 is:",filterData)
if __name__=="__main__":
    main()