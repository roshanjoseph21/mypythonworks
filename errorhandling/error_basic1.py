n1=int(input("Enter the first number---->>>"))
n2=int(input("Enter the second number--->>>"))
lst=[10,20,56]
loc=int(input("Enter the index position of fact object---->>>"))
try:
    print(lst[loc])
except Exception as e:
    print(e.args)
try:
    res=n1/n2
    print(f"result={res}")
except Exception as e:
    print("exception occured")
print("database committ")
print("file transaction")