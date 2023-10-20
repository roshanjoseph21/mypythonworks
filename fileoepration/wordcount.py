f=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\fileoepration\\news.txt")
wc={}
for line in f:
    words= line.rstrip("\n").split(" ")
    for w in words:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1
print(wc)
