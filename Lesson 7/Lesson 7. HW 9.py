print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# 
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
c = 0
salary = 0
c1 = 0
for n in range(10):
    salary = int(input("Введите число: "))
    c += salary
    c1 = c - salary
    print(c1,c)
    if(c1 > c):
        print("Бух, тебя наё :)")  
        break
    
