lst1=[10,23,34,45,67,87,54,43,33,5,43]
lst2=[20,34,54,43,25,67,87,32,33,67,7]

st_lst1=set(lst1)
st_lst2=set(lst2)

diff_set=st_lst1.difference(st_lst2)
print(diff_set)