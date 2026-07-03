def area(Radius,PI):
    ans=PI*Radius*Radius
    return ans

def main():
    ret=area(10.5,3.14)
    print("Area of circle:",ret)

if __name__=="__main__":
    main()