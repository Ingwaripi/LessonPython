#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, 
# без строк.Без использования встроенной функции преобразования, без строк.
#in
#88
#out
#1011000
#in
#11
#out
#1011

def trans(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
        
    return bit[::-1] # print(*bit, sep="") - вывод знаначений без скобок и разделителей

result = trans(int(input("Enter number:")))
print(result)