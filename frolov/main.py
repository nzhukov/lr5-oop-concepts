from abc import ABC


class Vehicle(ABC):

    def __init__(self, brand, model, color, horsepower):
        self.brand = brand
        self.model = model
        self.color = color
        self.horsepower = horsepower

    def engine_on(self):
        print(f"{self.brand} {self.model} был заведен")

    def engine_off(self):
        print(f"{self.brand} {self.model} был заглушен")


class Car(Vehicle):

    def drive(self):
        print(f"{self.brand} {self.model} поехал")


class Airplane(Vehicle):

    def fly(self):
        print(f"{self.brand} {self.model} полетел")


class Ship(Vehicle):

    def sail(self):
        print(f"{self.brand} {self.model} поплыл")


car = Car("BMW", "X5", "Black", 300)
airplane = Airplane("Boeing", "747", "White", 1000)
ship = Ship("Titanic", "Titanic", "White", 10000)

car.engine_on()
car.drive()
car.engine_off()

airplane.engine_on()
airplane.fly()
airplane.engine_off()

ship.engine_on()
ship.sail()
ship.engine_off()
