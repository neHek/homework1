#!/usr/bin/python

k=int(input("Число: "))
simp_numb=[1,2,3]
for i in range(4,k):
    for j in range(1,len(simp_numb)):
        if i%simp_numb[j]==0:
            break
        elif (i%simp_numb[j]!=0) and (j+1==len(simp_numb)):
            simp_numb.append(i)

print(simp_numb)

                


