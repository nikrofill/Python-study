n = 50
a = 0
print("Загадай число от 1 до 100")
while a != 1:
    if(a == 2 and n >= 50):
        n = int((100 - n) * 0.5 + n)
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
    if(a == 2 and n < 50):
        n = int((50 - n) * 0.5 + n)
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
#___________________________________________________________________
    elif(a == 3 and n > 50):
        n = int(n - (100 - n) * 0.5)
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))   
    elif(a == 3 and n <= 50):
        n = int(n * 0.5)
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))  
#___________________________________________________________________
    elif(a == 0):
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
        continue
#___________________________________________________________________
if(a == 1):
    print("Я угадал, ура!")

    