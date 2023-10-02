import math as m
class Triangle:#Создание класса Triangle
    def __init__(self, a = 1, b = 2, c = 3):#Определяем три аргумента
        self.a = a#Передает значение 1
        self.b = b#Передает значение 2
        self.c = c#Передает значение 3
    def perimetr(self):#Определяем метод perimetr
        return self.a + self.b + self.c#Возвращает сумму сторон треугольника
    def square(self):#Определяем метод square
        p = self.perimetr()/2
        return m.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))#Площадь треугольника
triangle_1 = Triangle()
p = triangle_1.perimetr()#Создаем переменную p
s = triangle_1.square()#Создаем переменную s
print(f'P = {triangle_1.a} + {triangle_1.b} + {triangle_1.c}, P = {p}')#Выводим периметр треугольника
print(f'S = sqrt({p}({p}-{triangle_1.a})({p}-{triangle_1.b})({p}-{triangle_1.c})), S = {s}')#Выводим площадь треугольника
