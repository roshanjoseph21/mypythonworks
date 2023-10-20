f=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\fileoepration\data.txt","r")

# for line in f:
#     print(line)
# f.close()

words=[line.rstrip("\n") for line in f]
print(words)