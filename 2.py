'''print("Введите числа для сравнения")
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
    --i'''

print("Введите числа для сравнения")
try:
        arr = (input().split(' '))
        
except TypeError:
        print('<Вводите числа!>')
        
flag = None
for i in range(len(arr)):
        if (arr[i] >= arr[i+1]):
                flag = 1
        break
if flag is None:
        print('True')
else:
	print('False')
