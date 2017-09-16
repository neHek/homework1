#!/usr/bin/python

a=int(input('Первое число: '))
b=int(input('Второе число: '))

for i in range(a, b+1):
    if i%5==0:
        print(i)
