from re import *
text= "abcabcdcbaacaacbbbbb"
pattern="a+"  #ttimes of a
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

from re import *
text= "abcabcdcbaacaacbbbbb"
pattern="a*"  #match for any number of a
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


from re import *
text= "abcabcdcbaacaacbbbbb"
pattern="a?"  #
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())