print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

c = 0
card = 0
for n in range(10):
    card = int(input("Введите число: "))
    c += 1
    #print(card,c)
    if(card != c):
        print("Стоп. Потеряна карточка №", c)  
        break
    