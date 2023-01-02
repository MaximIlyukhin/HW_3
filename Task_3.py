# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = input().split()
b = []
for i in range(0, len(a)):
    b.append(float(a[i]))
z = 0  # количество знаков после точки
for i in b:
    q = i * 10
    z += 1
    if q % 10 == 0:
        break
minn = 10**z
maxx = 0
for i in b:
    c = i * 10**z % 10**z
    if c > maxx:
        maxx = c
    if c < minn:
        minn = c
print(round((maxx - minn) / 10**z, z))
