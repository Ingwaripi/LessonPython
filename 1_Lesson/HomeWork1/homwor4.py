#4. Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21




xa = int(input("Введите х координату: "))
ya = int(input("Введите y координату: "))
xb = int(input("Введите х координату: "))
yb = int(input("Введите y координату: "))

c = (((xa-xb)**2)+((ya-yb)**2))**0.5
print(round(c,3))