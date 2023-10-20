num1=int(input("Enter a value:"))
num2=int(input("Enter a value:"))
hcf=1

sm_num=num1 if num1<num2 else num2
# lcm(num1,num2)=(num1*num2)/GCD(num1,num2)
for i in range(1,sm_num+1):
     if(num1%i==0) and (num2%i==0):
         hcf=i
lcm=(num1*num2)/hcf
print(lcm)

