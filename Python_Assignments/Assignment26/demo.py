class demo:
    Value=0
    def __init__(self,No1,No2):
        self.No1=No1
        self.No2=No2
    def fun(self):
        print(self.No1)
        print(self.No2)

    def gun(self):
        print(self.No1)
        print(self.No2)

obj1=demo(11,10)
obj2=demo(51,101)
obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()