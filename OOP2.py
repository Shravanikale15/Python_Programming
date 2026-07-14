class Demo:
    #Class Variable ,two ways to access self and class name best way is using class name
    Value1=10
    Value2=20

    def __init__(self):
        self.No1=11
        self.No2=21
    #Instance Method, it can access all
    def fun(self):
        print("Inside Instance Mathod named as Fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)
    
dobj=Demo()
dobj.fun()

