from os.path import split


class empoy:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def show(cls,string):
        return cls(string.split(",")[0],int(string.split(",")[1]))
o=empoy("afiya shaik",90000)
print(o.name)
print(o.salary)

str="shaik afiya,90000"

e2=empoy.show(str)## class method as a alternative constractor
print(e2.name)
print(e2.salary)





