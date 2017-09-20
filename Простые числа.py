#!/usr/bin/python

k=int(input("Число: ")) # Пользователь вводит число
simp_numb=[2,3] # Мы знаем, что они простые
for i in range(4,k+1): # Проходим по всем числам от 4 до пользовательского
    for j in simp_numb: # Делим на каждое простое число
        if i % j==0: # Делится - переходим к следующему
            break
    else:
        simp_numb.append(i)

print(simp_numb)

                


