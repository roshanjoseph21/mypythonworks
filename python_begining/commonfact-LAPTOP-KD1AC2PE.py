#common factors of 12,24


num1=int(input("Enter 1st num:-->"))
num2=int(input("Enter 2nd num:-->"))
hcf=1

sm_num=num1 if num1<num2 else num2

for i in range(1,sm_num+1):
    if(num1%i==0) and (num2%i==0):
        hcf=i
print(hcf)