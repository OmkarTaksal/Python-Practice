def Area(Redius,Pi):
    Ans=Pi*Redius*Redius
    return Ans
def main():
    Ret=Area(Pi=3.14,Redius=10.5)
    print("Area of circle is :",Ret)
    
if __name__=="__main__":
    main()