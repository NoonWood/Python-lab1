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
    c = int(a) 
    print (c, "Руб.", b, "Коп.")
