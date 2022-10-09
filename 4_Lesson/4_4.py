# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число
# В качестве разделителя используйте пробел.

#def check(line):
#    arr = line.split()
#    for i in arr:
#        if not i.strip("-").isdigit():
#            return []
#    return arr

#def min_max(array):
#    if array:
#        return min(array, key=int), max(array, key=int)
#    return []
#f = check("2 25 36 -52")        
#print(min_max(f))

# 2. Найдите корни квадратного уравнения Ax2 + Bx + C = 0 с помощью модуля.
# Запросите значения A,B,C 3 раза. Уравнения и корни запишите в фаил

#from math import sqrt

#def abc(a, b, c):
#    D = b ** 2 - 4*a*c
#    with open("result.txt", 'a', encoding='utf-8') as my_f:
#        my_f.write(f"{a}x^2 + {b}x + {c} = 0\n")
#        if D > 0 and a:
#            my_f.write(str((-b + sqrt(D)) / (2 *  a))+"\n")
#            my_f.write(str((-b - sqrt(D)) / (2 * a))+"\n") 
#        elif D == 0 and b:
#            my_f.write(str(-b / (2 * a))+"\n")
#        else:
#            my_f.write("Корней нет\n")

#for i in range(3):
#   abc(int(input()), int(input()), int(input()))

# 3. Задайте 2 числа. Напишите программу, которая должна находить НОК(наименьшее общее кратное)
# этих двух чисел

import math

a = int(input())
b = int(input())

print(a * b // math.gcd(a, b))

