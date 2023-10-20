# word= "goodmorning"  
# len=len(word)
# for i in range(0, len):  
#     count = 1                    #Counts each character present in the string
#     for j in range(i+1, len):  
#         if(word[i] == word[j] and word[i] != " "):  
#             count = count + 1  
#             # #Set string[j] to 0 to avoid printing visited character 
#             word = word[:j] + " " + word[j+1:] 
#     if(count > 1 and word[i]!= " "):  
#         print(word[i])

word="hellooiinn"
srt=sorted(word)
count=len(word)

for i in range(0,count-1):
    j=i+1
    if(srt[i]==srt[j]):
        print(srt)