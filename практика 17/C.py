s = input("Введите строку:")
f = False
c = 0
for i in range(len(s)):
    if s[i] != " " and not (f):
        c += 1
        f = True
    elif s[i] == " ":
        f = False
print(f'Самое длинное слово:, длина {c}')
