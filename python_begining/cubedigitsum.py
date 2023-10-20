# num=int(input("ENTER A NUMBER:--"))
# sum=0
# while(num!=0):
#     last_digit=num%10
#     sum=sum+last_digit**3
#     num=num//10
# print(sum)


num=int(input("Enter a number :"))
sum=0
while(num!=0):
    last_digit=num%10
    cube=last_digit**3
    sum=sum+cube
    num=num//10
print(sum)    