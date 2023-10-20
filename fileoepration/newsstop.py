f_news=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\fileoepration\\news.txt",encoding="utf-8")
f_stop=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\fileoepration\\stopwords.txt",encoding="utf-8")

news_words=set()
stop_words={line.rstrip("\n") for line in f_stop}

for line in f_news:
    words=line.split()
    for w in words:
        news_words.add(w)

print(news_words.difference(stop_words))