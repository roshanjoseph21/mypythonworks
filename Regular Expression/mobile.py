# from re import *
# mob= input("ENTER A MOBILE NUMBER-->")
# pattern="[+]?(91)?[0-9]{10}"
# matcher=fullmatch(pattern,mob)

# if matcher ==None:
#     print("INVALID")
# else:
#     print("VALID")


from re import *
mob= input("ENTER A MOBILE NUMBER-->")
pattern="[0-9]{3}[-][0-9]{3}[-][0-9]{4}"
matcher=fullmatch(pattern,mob)

if matcher ==None:
    print("INVALID")
else:
    print("VALID")



