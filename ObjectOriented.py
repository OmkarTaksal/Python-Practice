class Arithematic:
    def Addition(No1,No2):
        Ans=No1+No2
        return Ans

    def Subtraction(No1,No2):
        Ans=No1-No2
        return Ans
    
aobj=Arithematic()

print("Enter 1st Number")
Value1=int(input())


print("Enter 2nd Number")
Value2=int(input())

Ret=aobj.Addition(Value1,Value2)            #Issue / Error
print("Addition is ",Ret)

Ret=aobj.Subtraction(Value1,Value2)         #Issue / Error
print("Subtraction is ",Ret)