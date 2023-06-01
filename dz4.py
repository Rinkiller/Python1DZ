# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(number):
    if number == 1: return False
    if number % 2 == 0:
        return False
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number

flag = True
while(flag):
    num = int(input('Введите число не более 100 тысяч: '))
    if num < 0 or num > 100000:
        print('Введите число из промежутка от 0 до 100 000')
    else: flag = False
print(is_prime(num))