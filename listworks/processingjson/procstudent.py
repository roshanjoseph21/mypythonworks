from json import load
path="C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\listworks\\processingjson\\student.json"
with open(path) as f:
    data=load(f)
    print(len(data))

all_name=[st.get("name") for st in data]
print(all_name)