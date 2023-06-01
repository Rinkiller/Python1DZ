# Елочка
num = int(input('Введите высоту елочки: '))
level = 1
for i in range(1,num + 1): 
    print(" " * (num  - i), '*' * level)
    level += 2
