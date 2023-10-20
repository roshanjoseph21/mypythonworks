text="ABACC"
lst=[]
duplicate_list=[]

for ch in text:
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
else:
    duplicate_list.append(ch)

print(duplicate_list[0])
