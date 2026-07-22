def area(Radius,PI):
    ans=PI*Radius*Radius
    return ans

def main():
    ret=area(PI=3.14,Radius=10.5)
    print("Area of circle:",ret)

if __name__=="__main__":
    main()