# Создать список из N натуральных чисел. Средичисел не хватает одного
# чтобы выполнять условие A[i] -1 = A[i-1].
# Найдите это число



# import random 


# def getArr():
#     path = 'LessonPy/5_Lesson/n5.txt'
#     data = open (path, 'r')
#     arr = list(map(int,(data.readline().split(' '))))
#     data.close()
#     arr.remove(random.choice(arr))
#     print(arr)
#     return arr

# def checkArr2(arr):
#     if arr[0]!=0:
#         return 0
    
#     for i in range(1,len(arr)):
#         if (arr[i]-1)!=arr[i-1]:
#             return arr[i]-1
#     return -1 

# print(checkArr2(getArr()))

# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элиментов менять нелбзя

from random import choices

def get_list(size):
    return choices(range(size*2), k=size)

def new_list(array):
    new_list = []
    for i in range(len(array)):
        some = array[i]
        arr = [some]
        for j in range(i+1,len(array)):
            if array[j] > some:
                arr.append(array[j])
                some = array[j]
        if len(arr) > 1: 
            new_list.append(arr)
    return new_list
d = get_list(10)
print(d,new_list(d), sep="\n")
