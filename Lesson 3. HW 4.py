print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2

print("Хочешь вычислить площадь треугольника?")
a = int(input("Введите длину первого катета: "))
b = int(input("Введите длину второго катета: "))
s = (a * b) / 2
print("Площадь треугольника равна: ", s)