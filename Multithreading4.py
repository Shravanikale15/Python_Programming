import threading
def display(no1,no2,no3): #def display(*No)
    print(f"Inside Display {no1},{no2}.{no3} :",threading.get_ident())
def main():
    print("Inside main:",threading.get_ident())
    tobj=threading.Thread(target=display,args=(11,21,51,))
    tobj.start()
if __name__=="__main__":
    main()