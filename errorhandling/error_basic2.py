n1=int(input("Enter the first number---->>>"))
n2=int(input("Enter the second number--->>>"))
try:
    res=n1/n2
    print(f"result={res}")
except Exception as e:
  n2=int(input("Enter value for second number--->>>"))
  res=n1/n2
  print(f"result={res}")
finally:
   print("database committ")
   print("file transaction")

