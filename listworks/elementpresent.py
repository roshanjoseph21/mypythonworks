lst=[12,23,34,56,78,90]
element=int(input("Enter then element"))
is_present="ELEMENT NOT PRESENT"

for i in range(0,len(lst)):
    if lst[i]==element:
        is_present="ELEMENT IS PRESENT"
        break
print(is_present)
