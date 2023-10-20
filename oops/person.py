class Person(object):

    def __init__(self,name):
        self.name=name

obj=Person("Hari")
print(obj.__class__)

lst=[10,30]
print(lst.__class__)

text="hello"
print(text.__class__)