class Human():
    def __init__(self,age):
        self.age=age
class Man(Human):
    def __init__(self,age):
        Human.__init__(self,age)

class Woman(Human):
    def __init__(self,age):
        Human.__init__(self,age)


def Creation():
    list_with_adam_and_eva=[]
    Adam=Man(20)
    list_with_adam_and_eva.append(Adam)
    Eva=Women(20)
    list_with_adam_and_eva.append(Eva)
    return list_with_adam_and_eva