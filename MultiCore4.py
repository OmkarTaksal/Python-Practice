import time 
import multiprocessing
import os

def SumCube(No):
    print("Process is Running with PID :",os.getpid())
    Sum=0
    
    for i in range(1,No+1):
        Sum=Sum+(i**3)
        
    return Sum
    



def main():
    
    Data=[100000000,200000000,300000000,400000000,500000000]
    Result=[]
    
    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()
    Result=pobj.map(SumCube,Data)
    pobj.close()
    pobj.join()
    
    end_time=time.perf_counter()
    print("result is ")
    print(Result)
    
    print(f"Time Required : {end_time-start_time:.4f}")
    

if __name__=="__main__":
    main()