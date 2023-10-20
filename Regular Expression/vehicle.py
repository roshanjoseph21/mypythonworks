from re import *
varname= input("ENTER A NUMBER-->")
pattern="[K-N]{2}[0-9]{2}[A-Z][0-9]{4}"
matcher=fullmatch(pattern,varname)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")