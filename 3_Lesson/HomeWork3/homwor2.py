#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#in
#4
#out
#[2, 5, 8, 10]
#[20, 40]

from random import sample

def set_list(count):
    
    if count < 0:
        print("Enter a positive number")
        return []
    
    arrey = sample(range(1,count * 2), count)
    return (arrey)

def prod_pairs(array: list):
    res_list = []
    len_list = len(array)

    for i in range(len_list // 2):
        res_list.append(array[i] * array[len_list - i - 1])

    if len_list % 2:
        res_list.append(array[len_list // 2])
    return res_list

new_list = set_list(int(input('Enter the number: ')))
print(new_list)
print(prod_pairs(new_list))
