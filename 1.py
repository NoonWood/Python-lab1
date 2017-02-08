class Err(Exception):
    pass
while 1:
    print('Введите число')
    try:
        a = float(input())
    except ValueError:
        print('<Вводите числа!>')
    else:
        try:
            if a<0:
                raise Err
        except Err:
            print('Некорректный формат!')
        else:
            b = int((a - int(a))*100)
            print (int(a), "Руб.", b, "Коп.")
