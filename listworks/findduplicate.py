# #sort 
# #find duplicate in two list

l1=[20,35,40,24,60]
l2=[45,35,98,40,55]

l1.sort()
l2.sort()

p1,p2=0,0

while(p1<len(l1) and p2<len(l2)):
    if l1[p1]==l2[p2]:
        print("The common element is",l1[p1])
        p1=p1+1
        p2=p2+1
    elif l1[p1]<l2[p2]:
        p1=p1+1
    else:
        p2=p2+1