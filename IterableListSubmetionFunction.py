def Summetion(No):
    Sum=0
    
    for i in No:
        Sum=Sum+i
    print(Sum)

def main():
    
    Marks=[78,90,56,98,77]
    Sum=0
    Ret=0
    
    Ret=Summetion(Marks)
    print("Addition is :",Ret)
    
        
if __name__=="__main__":
    main()
