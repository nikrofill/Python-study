print('Задача 4. Календари')

# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.
 
# Напишите программу,
# которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.
a = True
c = 0
while a != 0:
    a = int(input("Введите число: "))
    if (a == 0):
        break
    elif (a % 2 == 0):
        #print ("Четное")
        c += 1
print(c)