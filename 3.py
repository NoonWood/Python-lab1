class Err(Exception):
    pass

while 1:
    Num = input('Введите номер дебетовой карты (16 цифр)')
    try:
        intNum = int(Num)
    except ValueError:
        print('Вводите числа')
    else:
        try:
            strNum = str(Num)
            if len(strNum)!= 16:
                raise Err
        except Err:
            print('Введите 16 цифр')
        else:
            print('Номер>> ',strNum[0:4],'*' * 12,strNum[11:15])
            break
