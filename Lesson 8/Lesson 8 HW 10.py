from typing import Text


print('Задача 10. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
# 
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
# 
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
# 
# 
# Пример 1:
# 
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
# 
# Пример 2:
# 
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
# 
# Пример 3:
# 
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

b = int(input("Кол-во мальчиков: "))
g = int(input("Кол-во девочек: "))
c = ""
#print (b/g, g/b)
if (b / g >= 2 or g / b >= 2):
    print("Нет решений.")
else:
    if(b>g):
        for n in range(b-1):
            c += "BG"
        print (c+"B")
    elif(g>b):
        for n in range(g-1):
            c += "GB"
        print (c+"G")
    else:
        for n in range(b):
            c += "BG"
        print (c)