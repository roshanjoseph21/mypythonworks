lst=[10,11,12,13,14,15,16]

num=3
for i in range(0,len(lst)):
    if num==lst[i]:
        print("ELEMENT FOUND")
        break
else:
        print("ELEMENT NOT FOUND")
