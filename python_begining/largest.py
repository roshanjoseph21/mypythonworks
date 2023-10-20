num1=30
num2=20
num3=40

print((num1>num2)and(num1>num3))
print((num2>num1)and(num3>num2))
print((num3>num1)and(num3>num2))

# gcd(a,b)= (a*b)/LCM(a,b)
# LCM = (num1*num2)/HCF(num1,num2)
# Leapyear= if((year%400==0)or(year%100!=0)and(year%4==0)) print("The given year is leap year")