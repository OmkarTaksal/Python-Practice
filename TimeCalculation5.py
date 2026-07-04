# 5: 1 * 2 * 3 * 4 * 5   
import time
def Factorial(No):
    Fact=1
    
    for i in range(1,No+1):
        Fact=Fact*i
    return Fact

def main():
    Value=int(input("Enter the Number:"))
    Ret=Factorial(Value)
    start_time=time.perf_counter()
    print(f"Factorial of {Value } is {Ret}")
    end_time=time.perf_counter()  
    print(f"Time Required is: {end_time-start_time:.5f} second")

if __name__=="__main__":
    main()
    