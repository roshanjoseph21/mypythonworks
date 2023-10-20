from json import load

path="C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\product\\items.json"
with open(path,encoding="utf-8") as f:
    data=load(f)

filtered_items=[item["title"] for item in data if item.get('category')=="women's clothing" and 10<= item.get('price')<=30]
for title in filtered_items:
    print(title)