print('Задача 4. С заботой о природе')

# Огромный заповедник поделён на большое количество секторов.
# И у каждого сектора есть номер.
# Мы ответственны за группу секторов с номерами с 30-го по 35-ый
# и нам нужно следить за тем, чтобы посетителей в каждом секторе было меньше 10.
# А заодно и фиксировать для общей статистики, сколько раз это правило было нарушено.
# 
# Напишите программу,
# которая для каждого сектора запрашивает текущее количество людей в нём,
# и если оно больше 10, то фиксирует нарушение.
# В конце выведите количество нарушений
# 
# Пример:
# 
# Людей в 30 секторе: 7
# Всё спокойно.
# Людей в 31 секторе: 11
# Нарушение! Слишком много людей в секторе!
# Людей в 32 секторе: 100
# Нарушение! Слишком много людей в секторе!
# Людей в 33 секторе: 10
# Всё спокойно.
# Людей в 34 секторе: 0
# Всё спокойно.
# Людей в 35 секторе: 1
# Всё спокойно.
# Количество нарушений: 2

a = 0
c = 1
for n in range(30,36,1):
    a = int(input("Сколько людей в секторе " + str(n) + " ?" ))
    if (a > 10):
        c += 1
        print ("Нарушение! Слишком много людей в секторе!")
    else:
        print ("Всё спокойно.")
print("Всего нарущений:", c)