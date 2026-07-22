def area(Radius,PI=3.14):
    ans=PI*Radius*Radius
    return ans

def main():
    ret=area(10.5)
    print("Area of circle:",ret)

    ret=area(10.5,7.12)
    print("Area of circle:",ret)

if __name__=="__main__":
    main()