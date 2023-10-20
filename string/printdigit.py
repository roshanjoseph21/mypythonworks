text="I Have 2 bike and 3 cars and one elephant"

word=text.split(" ")
for w in word:
    if w.isdigit(): #print digits in the string
        print(w)