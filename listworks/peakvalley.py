lst=[2,4,3,5,6,8,6]

count=0               #print peak and valley homework

for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]
    if x<y>z or x>y<z:
        count=count+1
print(count)
