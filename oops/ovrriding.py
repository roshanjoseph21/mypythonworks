class Parent:
    def mobile(self):
        print("SAMSUNG S23")


    def car(self):
        print("ALTO")


class Child(Parent):
    def mobile(self):
        print("IPHONE 155")

ch=Child()
ch.mobile()
ch.car()


print("----------------------------------THIS IS NEXT PROGRAM-------------------------------")



class Parent:
    def vehicles(self):
        self.context=["Passionpro","Swift"]
        return self.context
    
class Child(Parent):

    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("OLA")
        return self.context
    
p=Parent()
print(p.vehicles())
c=Child()
print(c.vehicles())
