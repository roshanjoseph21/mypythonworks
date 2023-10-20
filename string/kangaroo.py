sourceword="chicken"
word="hen"
ls=len(sourceword)
for i in range(ls-2):
    for j in range(i+1, ls-1):
        for k in range(j+1, ls):
            str= sourceword[i]+sourceword[j]+sourceword[k]
if str==word:
    print("Source word is kangaroo of word")
else:
    print("Source word is not kangaroo of word")
        



