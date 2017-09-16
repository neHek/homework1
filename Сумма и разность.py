#!/usr/bin/python

PlusMin = input('Введите знак: ')
Numbers = input('Два целых числа через пробел: ')
Numbers = Numbers.split()

if PlusMin == '+':
    Result = int(Numbers[0]) + int(Numbers[1])
elif PlusMin == '-':
    Result = int(Numbers[0]) - int(Numbers[1])
else:
    print('Только + и -')
    Result = ''

print(Result)
