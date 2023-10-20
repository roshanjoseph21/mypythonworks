name= "LuMiNaR TeChNoLOgIeS"
print(name.casefold()) #uppercase to lowercase

print(name.capitalize()) #set firstcharacter to uppercase

print(name.count('a')) #print number of character specified

print(name.startswith('Lu')) #check the begining of the string

print(name.endswith('eS')) #check the end of string

print(name.isalpha()) #check if all characters are alphabets

print(name.isdigit()) #check if all characters are digits 

print(name.isalnum()) #check if string contains only numbers and alphabets


name="HI How are you"

words=name.split(" ") #print words one by one
for w in words:
    print(w)


    