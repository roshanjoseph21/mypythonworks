expenses=[12000,11000,24000,35000,25000,21000]
# count=len(expenses)
# for i in range(0,count):
#     print(expenses[i])

# expenses[1]=150000
# print(expenses)


#total printing

total=0
for i in range(0,len(expenses)):
    total=total+expenses[i]
print(total)

totally=sum(expenses)
print(totally)

min_exp=min(expenses)
print(min_exp)

max_exp=max(expenses)
print(max_exp)

srt=sorted(expenses)
print(srt)

d_srt=sorted(expenses,reverse=True)
print(d_srt)
