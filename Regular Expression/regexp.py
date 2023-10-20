from re import *
text= "ababcdAbabc"
pattern="ab"
times=0
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start())
    times=times+1
print(f"Number of times pattern repeated={times}")

from re import *
text= "abcabABC K@234"
pattern="[a-d]"  #checkk pattern from a to d
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())



from re import *
text= "abcabABC K@234dfgdfgffgffhg"
pattern="[a-z]"  #checkk pattern from a to z
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


from re import *
text= "abcabABC ZSEFEHHDGFJGGK@234"
pattern="[A-Z]"  #checkk pattern from uppercase A TO Z
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


from re import *
text= "abcabABC 6463537wK@234"
pattern="[0-9]"  #checkk number nd location
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())



from re import *
text= "abcabABC K@234"
pattern="[a-zA-Z0-9]"  #checkk pattern from  a-z A-Z 0-9
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


from re import *
text= "abcabABC K@234"
pattern="[^a-z]"  #exclude provided thingd
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())



from re import *
text= "abcabABC K@234"
pattern="[^a-zA-Z]"  #exclude provided thingd
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())



from re import *
text= "abcabABC!@#$%^&*(K@234"
pattern="[^a-zA-Z0-9]"  #TO PRINT SPCIAL CHARACTERS
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())



from re import *
text= "abcabABC K@234"
pattern="\d"  #predefined for check digits
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

from re import *
text= "abcabABC K@234"
pattern="\D"  #exclude digits
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


from re import *
text= "abcabABC K@234"
pattern="\w"  #all alphabets and numbers
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())



from re import *
text= "abcabABC K@234"
pattern="\W"  #exclude all alphabets and numbers #special characters
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())