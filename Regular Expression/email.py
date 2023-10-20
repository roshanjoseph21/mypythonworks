from re import *
mail= input("ENTER A EMAIL ID-->")
pattern="\w[@]gmail.com*"
matcher=fullmatch(pattern,mail)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")