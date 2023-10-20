# def add(*args):                #acceeppt any number of parameters
#     print(args)

# add(1,2,3,4,5,6,7,8,6,5,4,3,6,3,6,4,9)

def product(*args):
    res=1
    for n in args:
        res=res*n
    return res

print(product(10,20))
print(product(1,2,3,4,5,6,7))


def adder(*args):
    return sum(args)
print(adder(1,2)) 

def concat_string(*args):
    return "#" .join (args)

print(concat_string("hello","hai","hello"))

# def reverse_concat(*args):
#  print(reverse_concat("red","green","blue"))

lst=["red","green","blue"]
lst.reverse()

print(lst)

def person_name(**kwargs):
    print(kwargs)
person_name(first_name="sachin",middle_name="ramesh",last_name="tendulkar")

def empdetails(**kwargs):
    print(kwargs)
    name=kwargs.get("name")
    exp=kwargs.get("exp")
    dep=kwargs.get("dep")
    print(f"{name} has {exp} year exp in {dep}")

empdetails(name="john",exp="2",dep="web development")