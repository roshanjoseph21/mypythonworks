from re import *
varname= input("ENTER A VARIABLE-->")
pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,varname)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")