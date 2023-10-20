num=int(input("Enter a number"))

prime=[num%n==0 for n in range(2,num)]
print("Prime" if any(prime)==False else "Not prime")


