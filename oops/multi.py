class P1:
    def m1(self):
        print("Inside Parent1")

class P2(P1):
        def m1(self):
            print("Inside Parent 2")

class Child(P2):
        def m3(self):
            print("INSIDE CHILD)")


ch=Child()
ch.m1()
