num1=20
num2=34
print (f"values before swapping num1={num1}, num2={num2}")

temp=num1
num1=num2
num2=temp
print (f"values after swapping num1={num1}, num2={num2}")

num1=num1+num2
num2=num1-num2
num1=num1-num2
print (f"values after swapping num1={num1}, num2={num2}")