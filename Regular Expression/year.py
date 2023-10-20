from re import *
date= input("ENTER A DATE-->")
pattern="\d{4}[-\s]\d{2}[-\s]\d{2}"
matcher=fullmatch(pattern,date)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")