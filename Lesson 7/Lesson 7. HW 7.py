print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

a = int(input("Число a: "))
b = int(input("число b: "))
c = 0 #счетчик
c1 = 0 #сумму
for n in range(a,b,1):
    if n % 3 == 0:
            c += 1
            c1 += n
c = c1 / c
print("Среднее арифметическое:", c)