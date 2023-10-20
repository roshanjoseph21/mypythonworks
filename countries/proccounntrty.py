from json import *
path="C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\countries\\data.json"
with open(path,encoding="utf-8") as f:
    data=load(f)
print(len(data))

all_regions={c.get("region") for c in data}

asian_countries=[c.get("name") for c in data if c.get("region")=="Asia"]
print(asian_countries)

independent_countries=[c.get("name") for c in data if c.get("Independent")==True]
print(independent_countries)