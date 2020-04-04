import random #  Загружаем генератор случайных чисел
x_min = 0   # Определяем нижнюю границу диапазона случайных чисел
x_max = 100 # Определяем верхнюю границу диапазона случайных чисел
hide_number = random.randrange(x_min, x_max) # Загадываем случайное число
number = int((x_max-x_min)/2) # Первая попытка

count = 1   

while number!= hide_number:  # Мат алгоритм нахождения неизвестной
    if hide_number>number:
        x_min = number
        number = int(number + (x_max - x_min)/2)   
        count+=1

    else:
        x_max = number
        number = int(number - (x_max - x_min)/2)
        count+=1

print("Загаданное число", number, ". Вы угадали с", count, 'попыток.')
    