class Book:
    name:str
    author:str
    price:int
    publisher:str



    def set_book(self,name,author,price,publisher):
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher


    def display_book(self):
        print(self.name,self.author,self.price,self.publisher)
    def __str__(self):
        return self.name

obj1=Book("HARRY POTTER","CDF",1233,"EDF")
print(obj1)