for row in range(1,14):
    for sp in range(14,row-1,-1):
        print(end=" ")
    for col in range(1,row+1):
        print(" * ",end="")
    print()