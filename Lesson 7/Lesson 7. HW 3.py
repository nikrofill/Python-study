print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.

a1 = 0
for n in range(12):
    a = int(input("Введите число: "))
    a1 += a
a1 = a1 / 12
print("Средняя з/п составляет:", a1)
