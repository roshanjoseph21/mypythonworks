n=5
for row in range(1,n+1):
    for col in range(n-row):
        print("",end=" ")

    for k in range(2*row-1):
            if k==0 or k==2*row-2:
                 print("* ",end=" ")
            else:
                 if row==n:
                      print("* ",end=" ")
                 else:
                    print(" ",end=" ")
    print()