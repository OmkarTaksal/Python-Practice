print("_____________________________________________")
print("_______________Ticket Price__________________")
print("_____________________________________________")

print("Enter the Age :")
Age=int(input())

if(Age <=5):
    print("Free Entry :")
elif(Age>5 and Age<=18):
    print("Ticket price is : 900")
elif(Age>18 and Age<=40):
    print("Ticket price is : 1200")
else:
    print("Ticket price is : 500")