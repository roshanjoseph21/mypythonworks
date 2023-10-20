num=input("Enter the number:--")
digit_count=len(num)
num=int(num)
sum=0
org=num
while(num!=0):
    last_digit=num%10
    sum=sum+last_digit**digit_count
    num=num//10
print("The Number is armstong" if sum==org else "Not armstrong")

# num=input("Enter a number:")
# digit_count=len(num)
# num=int(num)
# org=num

# sum=0
# while(num!=0):
#     last_digit=num%10
#     power_digit=last_digit**digit_count
#     sum=sum+power_digit
#     num=num//10
# if org==sum:
#     print("")
