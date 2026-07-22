class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Circumference=0.0
        self.Area=0.0

    def Accept(self,Radius):
        self.Radius=Radius

    def CalculateArea(self):
        self.Area=self.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference=2*self.PI*self.Radius

    def Display(self):
        print("Value of Radius:",self.Radius)
        print("Value of Area:",self.Area)
        print("Value of Circumference:",self.Circumference)

obj1=Circle()
obj1.Accept(4)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()


obj2=Circle()
obj2.Accept(5)
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()



obj3=Circle()
obj3.Accept(7)
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()

