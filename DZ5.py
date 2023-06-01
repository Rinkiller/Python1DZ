# игра угадайка 
# загадываем число от 1 до 100 000
# комп угадывает
# каждый ход даем подсказки больше или меньше
def is_bigNumbeg():
    print('Это число больше? y - да ')
    res = input()
    if res == 'y': return True
    else: return False

def is_goodNumbeg(number1,number2):
    print('Ваше число - ', (number2 - number1) // 2 + number1,' y - да  ')
    res = input()
    if res == 'y': return True
    else: return False

print('Загадайте число из промежутка от 1 до 100 000')

flag = True
min = 0
num = 100000
step = 1
while(flag):
    print('Шаг №', step)
    if is_goodNumbeg(min, num): 
        print('Ураа я угадал')
        break
    if is_bigNumbeg(): min = (num - min) // 2 + min
    else: num = (num - min) // 2 + min
    step += 1
