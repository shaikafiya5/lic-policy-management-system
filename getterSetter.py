class info:
    def information(self,name,age):
        self.name=name
        self.age=age

    @property
    def get_age (self):
        return self.age,self.name

    @get_age.setter
    def get_age (self,value):
        self.age=value

a=info()
a.information("afiya", 21)
print(a.get_age)
a.get_age=23
print(a.get_age)









































