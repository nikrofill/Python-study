n1 = 0
n2 = 100
n = (n1 +n2) // 2
a = 0
print("Загадай число от 1 до 100")
#___________________________________________________________________
while a != 1:
    if(a == 2):
        n1 = n
        n = (n1 +n2) // 2
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
#___________________________________________________________________
    elif(a == 3):
        n2 = n 
        n = (n1 +n2) // 2
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))  
#___________________________________________________________________
    elif(a == 0):
        print (n)
        a = int(input("Я угадал (1) ? Больше (2) ? Меньше (3) ? "))
        n = (n1 +n2) // 2
        continue
#___________________________________________________________________
if(a == 1):
    print("Я угадал, ура!")

    