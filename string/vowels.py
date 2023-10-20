words="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels="a","e","i","o","u"
v_count=0
c_count=0
for ch in words:
    if ch in vowels:
        v_count=v_count+1
    elif ch.isalpha():
        c_count=c_count+1
print(f"TOTAL NUMBER OF CHARACTERS={len(words)}")
print(f"NUMBER OF VOWELS ={v_count}")
print(f"NUMBER OF CONSONANTS={c_count}")

