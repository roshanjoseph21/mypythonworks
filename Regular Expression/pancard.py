from re import *
pan= input("ENTER A PAN NUMBER-->")
pattern="[A-Z]{3}[PCAHFT]{1}[A-Z]{1}\d{4}[A-Z]{1}"
matcher=fullmatch(pattern,pan)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")
