lst=[3,4,5,6,7,8]

#print odd
odd=[num for num in lst if num%2!=0]
print(odd)
#print even
even=[num for num in lst if num%2==0]                    #with condition
print(even)

#cube
cube=[num**3 for num in lst]
print(cube)

#square
sq=[num**2 for num in lst]                     #list comprehension
print(sq)

#add two
add_two=[num+2 for num in lst]
print(add_two)