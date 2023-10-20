class Superheroes:
    def __init__(self,name):
        self.name=name

    def super_powers(self):
        self.context=["run","jump"]
        return self.context
    
class SpiderMan(Superheroes):

    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("fly")
        self.context.append("spread web")
        return super().super_powers(self)


class MinnalMurali(Superheroes):

    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("speed")
        self.context.append("strong")
        return super().super_powers(self)
    
sp=Superheroes()
sp.super_powers

