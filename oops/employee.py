class Employee:
    id:int
    name:str
    dept:str
    salary:int



    def set_employee(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary


    def display(self):
        print(self.id,self.name,self.dept,self.salary)

    def __str__(self):
        return self.name

emp1=Employee()
emp1.set_employee(1000,"Vinay","teach",1346757) 
print(emp1)
emp2=Employee()
emp2.set_employee(1001,"helta","manager",150000)
emp2.display()

print("------------------------------------NEXT PROGRAM-------------------------------------------")


class Employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept

    @property
    def get_name(self):
        return self.name
    
    @property
    def get_salary(self):
        return self.salary
    
emp=Employee("hari",450000,"qa")

print(emp.get_name)
print(emp.get_salary)