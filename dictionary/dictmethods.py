animals={"a":"apple","b":"banana","c":"cat","d":"dog","e":"elephant"}

for k in animals.keys():
    print(k)

print(animals.get("w"))

animals.pop("e")
print(animals)