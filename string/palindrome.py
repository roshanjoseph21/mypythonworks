word="abba"
count=len(word)
p_str=""
for i in range(count-1,-1,-1):
    p_str=p_str+word[i]
if word==p_str:
        print("PALINDROME")
else:
        print("NOT PALINDROME")