print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

a = int(input("Введите 4-х значное число: "))
b = int(a / 1000)
c = int(a / 100)
c = int(c % 10)
d = a % 100
d = int(d/10)
e = a % 10
e=e*1000
d=d*100
c=c*10
print(e+d+c+b)