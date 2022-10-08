#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#in
#5
#out
#[10, 2, 3, 8, 9]
#22


from random import sample

def set_list(count: int):
    if count < 0:
        print("Enter a positive number")
        return []

    arrey = sample(range(1,count * 2), count)
    return (arrey)


def sum_odd_pos(array: list):
    sum_nums = 0
    for k in range(0, len(array), 2):
        sum_nums += array[k]
    return sum_nums
all_list = set_list(int(input('Enter the number: ')))
print(all_list)
print(sum_odd_pos(all_list))
