class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
        
    def Addition(self):
        Ans=self.No1+self.No2
        return Ans

    def Subtraction(self):
        Ans=self.No1-self.No2
        return Ans

print("Enter 1st Number")
Value1=int(input())

print("Enter 2nd Number")
Value2=int(input())

aobj=Arithematic(Value1,Value2)

Ret=aobj.Addition()           
print("Addition is ",Ret)

Ret=aobj.Subtraction()        
print("Subtraction is ",Ret)