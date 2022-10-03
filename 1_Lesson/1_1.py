# 1. Напишите программу которая на вход принемает два числа
#    и проверяет, является ли одно число квадратом второго.
#a = int(input('Enter a: '))
#b = int(input('Enter b: '))
#c = a**2
#d = b**2

#if c == b:
    #print('a is sqare of b')
#elif a==d:
    #print('b is sqare of a')
#else:
    #print('No')

#a = int(input('Enter a: '))
#b = int(input('Enter b: '))

#if a == b**2 or b == a**2:
    #print('YES')
#else:
    #print('NO')

# 2.Напишите программу которая на вход принемает 5 чисел
#   и находит максимальное число из них

#max = 0
#for i in range(5):
    #n = int(input())
    #if n > max:
        #max = n
#print(f'max number = {max}')

# 3. Напишите программу которая будет на вход принемать число N
#    и выводить числа от -N до N

#n = int(input())
#for i in range(-n, n + 1):
#    print(i, end=" ")

# 4. Напишите программу которая на вход будет принемать дробь
#    и показывать превую цифру дробной части числа

#a = float(input())
#a = a * 10 % 10
#print(int(a))

# 5. Напишите программу которая принемает на вход  и проверяет,
#    кратно ли оно 5 и 10 или 15, но не 30

#a = int(input())
#if ((a % 5 == 0 and a % 10 == 0 or a % 15 == 0)) and (a % 30 != 0):
#    print('YES')
#else:
#    print('NO')

#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            if not (x == z or x <= y and z):
#                print(x, y, z)