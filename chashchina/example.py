# 1. Создаём простой класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Привет, меня зовут {self.name}")

# 2. СОЗДАЁМ ОБЪЕКТЫ
person1 = Person("Анна", 25)   # объект №1
person2 = Person("Иван", 30)   # объект №2
person3 = Person("Мария", 22)  # объект №3

# 3. Используем объекты
person1.greet()   # Привет, меня зовут Анна
person2.greet()   # Привет, меня зовут Иван
person3.greet()   # Привет, меня зовут Мария

# 4. Читаем атрибуты
print(person1.name)   # Анна
print(person2.age)    # 30