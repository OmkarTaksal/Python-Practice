#----------------------------------------------------
#                       List        Tupel
#----------------------------------------------------
#
# Order                 yes         yes
# Index                 yes         yes
# Muable                yes         No
#
#----------------------------------------------------


def main():
    Data1=[10,20,30,40,True,"Pune"]         #List
    Data2=(10,20,30,40,True,"Pune")         #Tupel
    
    print(Data1)
    print(Data2)
    
    print(Data1[0])
    print(Data2[0])
    
if __name__=="__main__":
    main()