class MathUtils:
    """
    Класс-утилита для математических операций.
    Не требует создания объектов — всё статическое.
    """
    
    # Статический атрибут (константа)
    PI = 3.14159
    
    @staticmethod
    def add(a, b):
        """Статический метод: сложение"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Статический метод: умножение"""
        return a * b
    
    @staticmethod
    def circle_area(radius):
        """Статический метод: площадь круга"""
        return MathUtils.PI * radius * radius

result1 = MathUtils.add(5, 3)           # 8
result2 = MathUtils.multiply(4, 7)      # 28
result3 = MathUtils.circle_area(10)     # 314.159

print(f"5 + 3 = {result1}")
print(f"4 × 7 = {result2}")
print(f"Площадь круга радиусом 10 = {result3}")
print(f"Число Пи = {MathUtils.PI}")