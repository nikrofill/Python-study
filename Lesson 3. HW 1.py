print('Задача 1. Язык математики')

# Маше для защиты курсовой работы нужно написать программу для расчёта экономической модели по формуле.
# Как записать саму формулу в программу, она не знает, у неё есть только начальные значения.
# Поэтому Маша решила просто заплатить Егору, чтобы тот написал её быстрее.
#
# Дана программа:
# a = 8
# b = 10
# c = 12
# d = 18
#
# Продолжите программу:
# переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.
#
# Выражение: 

# (-3 + a**2) * b - 2**3
#      c- 2 * d

a = 8
b = 10
c = 12
d = 18
res = [((a ** 2 - 3) * b -2 ** 3) / (c - 2 * d)]
print(res)