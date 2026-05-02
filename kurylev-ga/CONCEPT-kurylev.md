# Инкапсуляция в Python (пример с классом Person)

## Определение

**Инкапсуляция** — это принцип ООП, при котором внутреннее состояние объекта скрывается и доступ к нему осуществляется только через контролируемые методы (геттеры и сеттеры).
Это позволяет защищать данные от некорректного изменения и управлять логикой доступа.

---

## Реализация

```python
# Метод с геттером и сеттером
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.__age = age
        self.__height = height

    # Age getter and setter
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Недопустимый возраст")

    # Height(in cm) getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if 50 < height < 250:
            self.__height = height
        else:
            print("Недопустимый рост")

    def is_adult(self):
        return self.age >= 18


# Реализация
p = Person("Grisha", 20, 182)

print(p.is_adult())  # True

p.age = -5  # Недопустимый возраст
p.height = -190  # Недопустимый рост   
```

---

## Пример использования

```python
print(p.is_adult())  # True

p.age = -5  # Недопустимый возраст
p.height = -190  # Недопустимый рост
```

---

## Где здесь инкапсуляция

* Поля `__age` и `__height` скрыты от прямого доступа
* Изменение возможно только через сеттеры (`age`, `height`)
* В сеттерах реализована проверка данных
* Метод `is_adult()` использует внутреннее состояние объекта

Таким образом, объект сам контролирует свои данные и не допускает некорректных значений.

