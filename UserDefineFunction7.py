def Calculator(No1,No2):
    Mult=No1*No2
    Dvi=No1/No2
    return Mult,Dvi
    
    
def main():
    Value1=int(input("Enter the 1st Number:"))
    Value2=int(input("Enter the 2nd Number:"))
    
    Ret1,Ret2=Calculator(Value1,Value2)
    
    print("Multiplication is :",Ret1)
    print("Devision is :",Ret2)
    
if __name__=="__main__":
    main()