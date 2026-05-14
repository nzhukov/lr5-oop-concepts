# Наследование в ООП

Наследование — это один из ключевых принципов объектно-ориентированного программирования, который позволяет создавать новый класс на основе существующего, заимствуя его атрибуты и методы. Это способствует повторному использованию кода, уменьшает дублирование и упрощает расширение функциональности.

Класс, от которого наследуют, называется родительским (или базовым, суперклассом), а класс, который наследует — дочерним (или производным, подклассом). Дочерний класс может не только использовать поведение родителя, но и переопределять его методы или добавлять новые.

В приведённом примере базовый класс `Vehicle` определяет общие свойства (бренд, модель, цвет, мощность) и действия (запуск и остановка двигателя). Конкретные типы транспорта — `Car`, `Airplane`, `Ship` — наследуют эти свойства и расширяют их уникальным поведением: ехать, лететь, плыть.

## Пример кода

```python
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

# Использование
car = Car("BMW", "X5", "Black", 300)
car.engine_on()
car.drive()
car.engine_off()
```