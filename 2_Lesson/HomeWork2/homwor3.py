#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input())
listnum = []
sum = 0
for n in range(1, num +1):
    result = round((1 + 1 / n) ** n)
    listnum.append(result)
    sum += result
    
print(listnum) 
print(sum)

    
