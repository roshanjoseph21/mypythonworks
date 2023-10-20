from json import load

path="C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\product\\items.json"
with open(path,encoding="utf-8") as f:
    data=load(f)

print(len(data))    #print total number of products

all_categories={p.get("category") for p in data}
print(all_categories)

for pd in data:
 if pd.get("category").count("electronics")>0:
        print(pd.get("title"))


for p in data:
    if p.get("category")=="women's clothing" and p.get("price")>20 and p.get("price")<=30:
        print(p.get("title"))

most_revealed_product=max(data,key=lambda p:p.get("rating").get("count"))
print(most_revealed_product.get("title"))

srt_items=sorted(data,reverse=True,key=lambda p:p.get("price"))
for p in srt_items:
    print(p.get("title"))

wc={}
for p in data:
    category=p.get("category")
    if category not in wc:
        wc[category]=1
    else:
        wc[category]+=1
print(wc)
val_key=[(v,k) for k,v in wc.items()]
print(sorted(val_key))

#womens clothing price range 100,300

for p in data:
    if p.get("category")=="women's clothing" and p.get("price")>100 and p.get("price")<=300:
        print(p.get("title"))



