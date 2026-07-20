class Demo:
    # Class Veriable
    Value1=10
    Value2=20
    
    def __init__(self):
        self.No1=11
        self.No2=22
        
       # Instnce Method
    def fun(self):
        print("Inside instance methos name as Fun")
        print(self.No1)
        print(self.No2)
        print(self.Value1)
        print(self.Value2)
        
dobj=Demo()
dobj.fun()