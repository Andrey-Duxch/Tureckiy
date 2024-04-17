from random import randint
n = int(input("Введите количество элементов:\n"))
n = [randint(0, 10) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in n)}')
def A(n):
    max1 = 0
    c = 0
    for i in n:
        if i % 2 != 0:
            c += 1
            max1 = max(max1, c)
        else:
            c = 0
    return max1
r = A(n)
print(f"Длина наибольшего отрезка нечетных чисел равна: {r}")
