source_word="CHICKEN"
word="HENS"
is_kangaroo="The given word is a kangaroo word of source word"
source_word_list=[]
for ch in source_word:
    source_word_list.append(ch)

for ch in word:
    char_count=source_word_list.count(ch)

    if char_count>0:
        source_word_list.remove(ch)

    else:
        is_kangaroo="The given word is NOT A kangaroo word of source word"
        break
print(is_kangaroo)

