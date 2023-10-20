source_word="RACE" #LENGTH=SAMEE AND SORT=SAME THEN ANAGRAM
word="CARE"

if len(source_word)!=len(word):
    print("The words are not Anagram")
else:
    srt_sword=sorted(source_word)
    srt_word=sorted(word)
    if srt_sword==srt_word:
        print("The words are Anagram")
    else:
        print("The words are not Anagram")