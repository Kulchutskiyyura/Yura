class Car:
    
    def __init__(self, name, make,model):
        self.name=name
        self.make=make
        self.model=model
    def start(self):
        print("автомобіль стартував")
    def stop(self):
        print("автомобіль зупинився")

my_car=Car("mystang",4,"gt-126")
print(my_car.name)

class Person:
    def __init__(self,name):
        self.name=name
    def info(self):
        print(f"Hello my name is {self.name}")

Yura=Person("yura")
Yura.info()

class Auto:
    def __init__(self, name):
        self.name=name
    def move(self,speed):
        print(f"{self.name} move at speed {speed} km/h")

my_car_2=Auto("volga")
my_car_2.move(50)
  
