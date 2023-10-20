from re import *
f=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\Regular Expression\\dates.txt")
# pattern="\d{4}[-\s]\d{2}[-\s]\d{2}"
# pattern="(20)([01][0-9]|2[0-3])[-/](0[1-9]|1[0-2])[-/]\d{2}"
pattern="(20)([01][0-9]|2[0-3])[-/](0[1-9]|1[0-2])[-/]([0][1-9]|[12][0-9]|3[01])"
for line in f:
    date=line.rstrip("\n")
    matcher=fullmatch(pattern,date)
    if matcher!=None:
        print(date)





















    