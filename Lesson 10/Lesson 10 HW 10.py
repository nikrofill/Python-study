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

a = int(input("Введите число: "))
for n in range(a,0,-1):
    for n1 in range(n):
        print(n1, end="")
        #print((a-n1)*".")
        #print(n1, end="")
    
    print("\n")

