#builtin utilityfunctions 

expenses=12000,14000,56000,34000,45000,76000,25000

total_exp=sum(expenses)
print(total_exp)

largest_exp=max(expenses)
print(largest_exp)

smallest_exp=min(expenses)
print(smallest_exp)

srt=sorted(expenses)
print(srt)

d_sort=sorted(expenses,reverse=True)
print(d_sort)
