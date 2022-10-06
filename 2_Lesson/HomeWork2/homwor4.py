#4. Напишите программу, которая принимает на вход 2 числа. 
#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях(не индексах).
#Position one: 1
#Position two: 3
#Number of elements: 5
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 15

num = int(input("Enter the value of N: "))
n_1 = int(input("Position one: "))
n_2 = int(input("Position tho: "))

num_list = list(range(-num, num + 1))

print(num_list)
len_list = len(num_list)

if len_list >= n_1 > 0 and len_list >= n_2 > 0:
    print(num_list[n_1 - 1] * num_list[n_2 - 1])
else:
    print("There are not values for thise indexes!")
