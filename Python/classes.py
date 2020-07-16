class abc:
    counts=0;
    def __init__(self,name):
        abc.counts+=1
        self.name=name
    def remove(self):
        print(self.name+" has been removed")
        abc.counts-=1
    def greet(self):
        print("welcome "+self.name)
    @classmethod
    def count(cls):
        print(cls.counts)
a1=abc("Shubham")
a1.greet()
abc.count()
a2=abc("XYZ")
a2.greet()
abc.count()
a2.remove()
abc.count()

class derived: abc
d1=abc("abc")
d1.greet()
d1.count()