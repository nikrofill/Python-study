print('Задача 2. Максимум из трёх чисел')

# Как-то у нас уже было задание 
# на нахождение максимума из трёх чисел с помощью дополнительной переменной.
# Теперь, когда вы знаете намного больше,
# вы можете оптимизировать программу, не тратя память компьютера на лишние переменные.
 
# Напишите программу,
# которая находит максимум из трёх чисел, не используя дополнительные переменны

print ("Привет, Андрей!")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
print()
print("Самое большее число:")
if (a > b):
    if(a > c):
        print(a)
    elif(a<c):
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    elif(b<c):
        print (c)
elif(c>a):
    if(c>b):
        print(c)
    elif(c<b):
        print(b)

#вставил код из Lesson 4 HW 10. Тут без доп перменных :)