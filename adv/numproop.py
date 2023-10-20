lst=[i for i in range(1,8)]
print(lst)

#1 or 7 = holiday

out=["holiday" if i==1 or i==7 else "weekday" for i in lst]
print(out)