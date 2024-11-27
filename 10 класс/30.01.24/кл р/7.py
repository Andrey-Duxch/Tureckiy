s = int(input("Введите площадь прямоугольника:"))
b = input("Перестановки считать одинаковыми? да/нет:\n") == "да"
for i in range(1, int(s**(1/2)) + 1):
    for j in range(i, s//i + 1):
        if i * j == s:
            if b:
                print(f'Прямоугольник {i} * {j}')
            else:
                print(f'Прямоугольники {i} * {j}, {j} * {i}')



