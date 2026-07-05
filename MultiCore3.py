import time 


def SumCube(No):
    Sum=0
    
    for i in range(1,No+1):
        Sum=Sum+(i**3)
        
    return Sum
    



def main():
    
    Data=[100000000,200000000,300000000,400000000,500000000]
    Result=[]
    
    start_time=time.perf_counter()
    for Value in Data:
        Ret=SumCube(Value)
        Result.append(Ret)
    
    end_time=time.perf_counter()
    print("result is ")
    print(Result)
    
    print(f"Time Required : {end_time-start_time:.4f}")
    

if __name__=="__main__":
    main()