lst=[2,4,3,5,6,8,6]

count=0               #print peak and valley homework

for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]
    if x<y>z:
        print(f"The peak values are",x,y,z)

    if x>y<z:
        print(f"The valley values are",x,y,z)

