def Area(Redius,Pi):
    Ans=Pi*Redius*Redius
    return Ans
def main():
    Ret=Area(10.5,3.14)
    print("Area of circle is :",Ret)
    
    Ret=Area(13.6,3.14)
    print("Area of circle is :",Ret)
    
if __name__=="__main__":
    main()