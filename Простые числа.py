#!/usr/bin/python

k=int(input("Число: ")) # Пользователь вводит число
simp_numb=[1,2,3] # Мы знаем, что они простые
for i in range(4,k): # Проходим по всем числам от 4 до пользовательского
    for j in range(1,len(simp_numb)): # Делим на каждое простое число
        if i % simp_numb[j]==0: # Делится - перехолдим к следующему
            break
        elif (i%simp_numb[j]!=0) and (j+1==len(simp_numb)): # Не делится - добавляем в список
            simp_numb.append(i)

print(simp_numb)

                


