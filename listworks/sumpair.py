sum=int(input("ENTER THE SUM-->"))
lst=[2,4,5,3,6]
lst.sort()
low=0
upp=len(lst)-1

while low<upp:
    cur_sum=lst[low]+lst[upp]

    if cur_sum==sum:
        print("The Pairs are",lst[low],lst[upp])
        low=low+1
        upp=upp-1
    elif cur_sum<sum:
            low=low+1

    elif cur_sum>sum:
            upp=upp-1


