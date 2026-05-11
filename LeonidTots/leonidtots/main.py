class Engine:
    def start(self):
        return "Двигатель запущен"


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return self.engine.start()


car = Car()

print(car.drive())