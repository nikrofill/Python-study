print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям. 
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, 
# чтобы понять динамику роста или падения дохода. И так за каждый год. 
# 
# Надя решила, 
# что быстрее будет написать простую программу, которая сделает всё за неё.
# 
# 
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.
first_kv = input("Введите сумму за первый квартал: ")
second_kv = input("Введите сумму за второй квартал: ")
third_kv = input("Введите сумму за третий квартал: ")
fourth_kv = input("Введите сумму за четвертый квартал: ")
sum_first_half_year = int(first_kv+second_kv)
sum_second_half_year = int(third_kv+fourth_kv)
sum = sum_first_half_year / sum_second_half_year
print("Частное первого квартала ко второму равно: ", sum)
print("Удачной работы, Надя")