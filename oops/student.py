class Student:
    rol:int
    course:str
    total:int


    def __init__(self,rolnum,course,total):
        self.rol=rolnum
        self.course=course
        self.total=total
    def display(self):
        print(self.rol,self.course,self.total)

obj1=Student(10,"Django",450)
obj1.display()

obj2=Student(12,"Django",423)
obj2.display()