st1={"RED","GREEN","YELLOW"}
st2={"YELLOW","ORANGE","RED","GREEN"}
# union_set=st1.union(st2)
# print(union_set)


# intersction_set=st1.intersection(st2)
# print(intersction_set)

# #pop method to remove anyy element

# st1.pop()
# print(st1)

# #remove method used to remove specific element

# st1.remove("GREEN")
# print(st1)

#discard used to remove element and not return error if element is not present
# st1.discard("GREEN")
# print(st1)

#issubset used to check if given set is a subset of the set and return true or false
print(st1.issubset(st2))

#issuperset used to check if given set is a superset of the set and return true or false
print(st2.issuperset(st1))