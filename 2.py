print("Введите числа для сравнения")
i = 15
print(end ='>> ')
a = input()
while i > 1:
    print(end ='>> ')
    b = input()
    if a < b:
        print ('True')
    else:
        print ('False')
    a = b
    --i
