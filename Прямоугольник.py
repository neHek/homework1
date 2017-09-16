#!/usr/bin/python

inp = input('Две стороны прямоугольника через пробел:')
inp = inp.split(' ')
area = float(inp[0])*float(inp[1])
print('Площадь: %.3f' % area)

