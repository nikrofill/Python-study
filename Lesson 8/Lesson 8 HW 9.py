print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 
a = int(input("Число: "))
sum2 = 1
sum1 = 1
for n in range(1,7,1):
    sum2 = sum2 * (a-(2**n-1))
    sum1 = sum1 * (a-(2**n))
    print(n, 2**n-1, 2**n)
print("ответ: ", sum2 / sum1)