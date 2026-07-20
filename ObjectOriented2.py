class Arithematic:
    def Addition(self,No1,No2):
        Ans=No1+No2
        return Ans

    def Subtraction(self,No1,No2):
        Ans=No1-No2
        return Ans
    
aobj=Arithematic()

print("Enter 1st Number")
Value1=int(input())

print("Enter 2nd Number")
Value2=int(input())

#Ret=Addition(aobj,Value1,Value2)

Ret=aobj.Addition(Value1,Value2)            
print("Addition is ",Ret)

Ret=aobj.Subtraction(Value1,Value2)        
print("Subtraction is ",Ret)