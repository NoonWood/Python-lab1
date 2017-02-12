vvod_str = str(input('Введите строку\n')).split(' ')
print('слова длинее семи символов:\n')
for i in vvod_str:
    if len(i) > 7:
        print(vvod_str.pop(vvod_str.index(i)))
print('слова длиною от 4 до 7 символов:\n')
for i in vvod_str:
    if 4 <= len(i) <= 7:
        print(vvod_str.pop(vvod_str.index(i)))
print('слова длиною меньше 4 символов:\n')
for i in vvod_str:
    print(i)
