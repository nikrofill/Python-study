print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
a = int(input("Введите число: "))
for n in range(a+1):
    for n1 in range(n):
        print(n, end = " ")
    print("")
