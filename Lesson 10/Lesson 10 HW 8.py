print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

a = int(input("Высота: "))
b = 1
for n in range(a):
    print(a * " ", b * "#", end = "\n")
    b += 2
    a = a - 1