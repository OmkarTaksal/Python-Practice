def main():
    Ans=0
    try:
        print("Enter the Number")
        No1=int(input())
        print("Enter the Number")
        No2=int(input())
        
        Ans=No1/No2
        print("Devision is Successful")
    except ZeroDivisionError as zobj:
        print("Exception occured due to second operand is zero:",zobj)
        
    except ValueError as vobj:
        print("Exception occured due to invalid data type",vobj)
        
    except Exception as eobj:
        print("Exception occured by",eobj)
        
    finally:
        print("Inside Finally block")
        
        
        
    print("Devision is :",Ans)
if __name__=="__main__":
    main()