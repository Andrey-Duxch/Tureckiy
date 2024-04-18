s = input("Введите строку:")
n = s.split()
c = 0
b = ""
for i in range(len(n)):
    if len(n[i]) > c:
        c = len(n[i])
        b = n[i]
print(f'Самое длинное слово: {b}, длина {c}')
