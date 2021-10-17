import random
n = range(1,101,1)
n = 50
a = 0
print("Загадай число от 1 до 100")
while a != 1:
    if(a == 2):
        n = int(n * 1.5)
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
    elif(a == 3):
        n = int(n * 0.5)
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
    elif(a == 0):
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
        continue
if(a == 1):
    print("Я угадал, ура!")

    