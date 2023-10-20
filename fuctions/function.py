def add(n1,n2):
    return n1+n2

#cube  product divison sub smart_sub(subtract less from great) factrial leapyear 

def cube(n):
    return n**3

def product(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def sub(n1,n2):
    return n1-n2

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

def factorial(n):
    fact=1
    for i in range(i,n+1):
        fact=fact*i
    return fact

def is_leapyear(year):
    if year%100==0 and year%400==0:
        return"Leapyear"
    elif year%100!=0 and year%4==0:
        return"Leapyear"
    else:
        return"Not Leapyear"
    
