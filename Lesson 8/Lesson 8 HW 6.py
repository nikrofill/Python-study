print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.
b = 12
c = 0
a = int(input("Введите длину стороны письма: "))
while(a > b):
    a = a // 2
    c += 1
print (c*2) #две же стороны