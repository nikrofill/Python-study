print('Задача 5. Марсоход 2')

# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
# 
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
# 
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
# 
# Пример:
# 
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
print("Координаты робота: 8, 10")
x = 8
y = 10
wasd = ""
while wasd != "0":
    wasd = input("Куда идем: ")
    if (wasd == 'W' and x < 15) or (wasd == 'w' and x < 15):
        x += 1
    elif (wasd == 'S' and x >0) or (wasd == 's'and x >0):
        x -= 1
    if (wasd == 'A' and y > 0) or (wasd == 'a' and y > 0):
        y -= 1
    elif (wasd == 'D' and y < 20) or (wasd == 'd' and y < 20):
        y += 1
    print("Координаты робота: ", x, y, "| 0 - выход")
    
    
