lst=[1,2,3,4,6]

limit=len(lst)
i=0
while(i<limit):
    j=i+1
    for i in range(0,limit):
        if lst[j]-lst[i]==1:
            print("NUMBER MISSING is",limit+1)
        elif lst[j]-lst[i]!=0:
            print("MISSING NUMBER IS",lst[i+1])
            break
        
 