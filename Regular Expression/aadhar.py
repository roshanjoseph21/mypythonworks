from re import *
uid= input("ENTER A AADHAR NUMBER-->")
pattern="\d{4}[\s]?\d{4}[\s]?\d{4}"
matcher=fullmatch(pattern,uid)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")