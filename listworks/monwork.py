list= 2,3,4,5,6 #get if sum=7 get pair of numbers that sums up 
#            ,sum=6, [2,4]

count=len(list)
sum=int(input("Enter the sum-->"))

for i in range(0,count):
    for j in range(i+1,count):
        if(list[i]+list[j]==sum):
            print(list[i],list[j])
