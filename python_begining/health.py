gender="female"
tummy_size=35
buttock_size=75
value=tummy_size/buttock_size
print(value)

if(gender=="male"):
    if(value<=0.95):
         print("Low Health Risk")
    elif((value<=0.97)and(value>=1)):
         print("Moderate")
    elif(value>1):
         print("High")

if(gender=="female"):
     if(value<=0.80):
         print("Low Health Risk")
     elif((value<=0.81)and(value>=0.85)):
         print("Moderate")
     elif(value>0.85):
         print("High")
     

