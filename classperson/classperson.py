class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getter(self):
        return self.name+" age is "+str(self.age)

person=Person('Yura',18)
print(person.getter())

