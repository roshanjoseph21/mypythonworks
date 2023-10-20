text="Hello guys, thank you for downloading my product, I really appreciate you. Please note that this font is free for personal use only, which means you may use it for free as long as you don't use it for commercial purposes. If you are interested in this font you can get a full license here"
words=text.casefold().replace(",","").split(" ")
wc={}
for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)
stop_words={"the","a","for","to"}