print('Задача 2. Должники')

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк, 
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
# 
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.
b = True
a1 = int(input("Введите число: "))
a2 = int(input("Введите число: "))
a3 = int(input("Введите число: "))
a4 = int(input("Введите число: "))
a5 = int(input("Введите число: "))
a6 = int(input("Введите число: "))
a7 = int(input("Введите число: "))
a8 = int(input("Введите число: "))
a9 = int(input("Введите число: "))
a10 = int(input("Введите число: "))
c1 = 0 #счетчик чет пол
c2 = 0 #счетчик нечет пол
c3 = 0 #счетчик чет отриц
c4 = 0 #счетчик нечет отриц
for a in (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    if(a > 0):
        if a % 2 == 0:
            c1 += 1
            #print("Число четное положительное")
        else:
            c2 += 1
            #print("Число нечетное положительное")
    else:
        if a % 2 == 0:
            c4 += 1
            #print("Число четное отрицательное")
        else:
            c4 += 1
            #print("Число нечетное отрицательное")
print("Четных положительных:", c1)
print("Нечетных положительных:", c2)
print("Четных отрицательных:", c3)
print("Нечетных отрицательных:",c4)