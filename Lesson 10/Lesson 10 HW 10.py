print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
#попробуйте внутри запускать один цикл для того, чтобы составить строку из убывающих чисел
#затем второй цикл, чтобы добавить в строку возрастающие числа

n = int(input("Введите глубину ямы: "))
for i in range(n):
  for a in range(n, n -i -1, -1):
    print(a, end = "")
  c = 2 * (n - i - 1)
  print("." * c, end = "")
  for b in range(n - i, n + 1):
    print(b, end = "")
  print()

