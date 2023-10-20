lst=[1,2,3,4,6]

max_num=max(lst)

totalsum=max_num*(max_num+1)/2

cur_sum=sum(lst)

diff=totalsum-cur_sum

if diff==0:
    print("THE MISSING LEAST POSITIVE INTEGER IS",max_num+1)
else:
    print("THE MISSING LEAST POSITIVE INTEGER IS",diff)
