class Err(Exception):
    pass

print('Введите число')
try:
    a = float(input())
    if a<0:
        raise Err
except Err:
    print('Некорректный формат!')
else:
    b = int((a - int(a))*100)
    print (int(a), "Руб.", b, "Коп.")
