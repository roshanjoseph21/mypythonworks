num=int(input("Enter a number: "))
is_prime=True

for i in range(2,num):
    if(num%i==0):
        is_prime=False
        break
print(is_prime)

if(is_prime==True):
    print(f"{num} is Prime")
else:
    print(f"{num} is not Prime")