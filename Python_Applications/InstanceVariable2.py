class Marvellous:
    #class variable
    no1=11
    no2=12
    def __init__(self): #To have instance variable its compulsory to write construtor
        self.Value1=21  #instance variable
        self.Value2=51  #instance variable

print(Marvellous.no1)
print(Marvellous.no2)

#Object/Instance Creation
mobj1=Marvellous()
mobj2=Marvellous()
mobj3=Marvellous()

print(mobj1.Value1)
print(mobj2.Value1)