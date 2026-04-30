# Зависимость

Зависимость это когда один класс использует другой класс в своем методе.

## Пример на Python

```python
class Prototype:
    def clone(self):
        return Prototype()


class Creator:
    def create_copy(self, prototype: Prototype):
        return prototype.clone()


prototype = Prototype()
creator = Creator()

copy_object = creator.create_copy(prototype)

print(copy_object)
```

В примере `Creator` зависит от `Prototype`, потому что метод `create_copy()` принимает объект `Prototype` и вызывает у него `clone()`.

Особенность Python: тип `prototype: Prototype` является подсказкой, но Python не проверяет его строго во время выполнения.
