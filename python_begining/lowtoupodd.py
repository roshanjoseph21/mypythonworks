low=int(input("Enter Lower Limit"))
upp=int(input("Enter Upper limit"))
for num in range(low,upp+1):
    if(num%2!=0):
        print(num)