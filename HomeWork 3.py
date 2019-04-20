#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9a = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i%j == 0:
            a[j-2] += 1

i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1



#2. Поменять местами минимальный и максимальный элементы
from random import random
n = 15
arr = [0]*n
for i in range(n):
    arr[i] = int(random()*100)
    print(arr[i], end = ' ')
print()

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print(f'arr[{imn+1}] = {mn} arr[{imx+1}] = {mx}')
