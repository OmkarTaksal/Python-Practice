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
            print(Demo.Value1)
            print(Demo.Value2)
            
    @classmethod        
    def gun(cls):
            print("Inside Class methos name as Gun")
           # print(Demo.No1)            Not Allowed
            #print(Demo.No2)            Not Allowed
            print(cls.Value1)
            print(cls.Value2)
    
    @staticmethod
    def Sun():
            print("Inside instance methos name as Sun")
            print(Demo.Value1)
            print(Demo.Value2)
        
 
 
# Call with object 
Demo.Sun()         
dobj=Demo()     
Demo.gun()