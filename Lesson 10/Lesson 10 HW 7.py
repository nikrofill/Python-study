from re import X


print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

x = 0
a = True
while a != 0:
    a = int(input('Введите натуральное число, для выхода введите 0: '))
    b = a
    s = 0
    while b > 0:
        b1 = b % 10
        b = b // 10
        s += b1
    print('Сумма числа =', s)   
    if s > x:
        x = s
        a1 = a
print('Наибольшее число =', a1, 'его сумма =', x)