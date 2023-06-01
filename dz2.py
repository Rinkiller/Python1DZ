# таблица умножения
a = [2,6]
string = ''
strPlus = '  '
strPlus1 = ' '
strPlus2 = ' '
for i in a:
    for j in range(0,11):
        for n in range(0,4):
            if j == 10: 
                if n == 0: 
                    strPlus = '  '
                    strPlus1 = ''
            if (i + n)*j > 9 : strPlus2 = ''
            string = string + " " + strPlus + str(i + n) + " * " + strPlus1 + str(j) + " = " + strPlus2 + str((i + n) * j)
        print(string)
        string = ''
        strPlus = '  '
        strPlus1 = ' '
        strPlus2 = ' '
    print()