class A:
    __new_dict={}

    def __init__(self):
        self.__dict__=self.__new_dict
        self.state="default"
    
    def __str__(self):
        return self.state

    def print_dict(self):
        return self.__new_dict

a=A()
b=A()
c=A()
a.state="a"
print(a)
print(b)
print(c)
print(c.print_dict())